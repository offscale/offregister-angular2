from sys import version

if version[0] == "2":
    from cStringIO import StringIO

else:
    from io import StringIO

from distutils.sysconfig import get_python_lib
from os import path

from fabric.contrib.files import cd, exists, shell_env
from fabric.operations import env, get, put, run
from offregister_fab_utils.apt import apt_depends
from offregister_fab_utils.git import clone_or_update
from offregister_nginx.ubuntu import setup_nginx_conf2 as _setup_nginx_conf2
from offutils import validate_conf


def install_nodejs0(*args, **kwargs):
    apt_depends("ca-certificates", "curl")
    run("mkdir -p $HOME/Downloads")
    if not exists("$HOME/n"):
        remote_loc = "$HOME/Downloads/n-install"
        run(
            "curl -L https://git.io/n-install -o {remote_loc}".format(
                remote_loc=remote_loc
            )
        )
        run("bash {remote_loc}".format(remote_loc=remote_loc))

    env.shell = "/bin/bash -l -i -c"  # Damn, this is global. TODO: find an alternative
    if run(
        """
    curl -s https://nodejs.org/dist/latest/ \
    | sed -n 's:.*<a href=\".*\">node-v\(.*\).pkg</a>.*:\\1:p' \
    | grep -- "$(ls $HOME/n/n/versions/node)"
    """,
        warn_only=True,
    ).failed:
        run("n latest")

    run("npm install -g webpack")


def _get_repo_name(kwargs):
    rfind = kwargs["GIT_REPO"].rfind(".git")
    l = kwargs["GIT_REPO"].rfind("/") + 1
    return kwargs["GIT_REPO"][l:rfind] if rfind > -1 else kwargs["GIT_REPO"][l:]


def _get_server_dir(**kwargs):
    return kwargs.get(
        "SERVER_LOCATION",
        "/var/www/static/{}".format(
            kwargs.get("nginx-init-context", {}).get(
                "NAME_OF_BLOCK",
                kwargs.get("nginx-conf-context", {}).get(
                    "NAME_OF_BLOCK", _get_repo_name(kwargs)
                ),
            )
        ),
    )


def _validate(f):
    def validate(*args, **kwargs):
        required = (
            ("GIT_REPO", "https://github.com/org/git-repo.git"),
            ("SERVER_LOCATION", "`unix:/run/my-server.sock` or `http://0.0.0.0:8080`"),
        )
        validate_conf(kwargs, required, name="kwargs")

        return f(*args, **kwargs)

    return validate


@_validate
def git_static1(*args, **kwargs):
    server_dir = _get_server_dir(**kwargs)
    clone_or_update(
        repo=kwargs["GIT_REPO"],
        to_dir=server_dir,
        branch=kwargs.get("GIT_BRANCH", "master"),
        use_sudo=True,
    )


@_validate
def _start_node2(*args, **kwargs):
    server_dir = _get_server_dir(**kwargs)

    # Don't use this in production! - Build a dist and deploy that
    with cd(server_dir), shell_env(SOCK_URL=kwargs["SERVER_LOCATION"]):
        run("npm i")
        # "app.set('SOCK_URL', undefined);", "app.set('SOCK_URL', '{SERVER_LOCATION}');"
        """
        sed('src/server.ts', ', undefined', ', "{SERVER_LOCATION}"'.format(
            SERVER_LOCATION=kwargs['SERVER_LOCATION']
        ), use_sudo=True)
        """
        """sudo('''
        sed -i src/server.ts -r -e "s|, undefined|, '{SERVER_LOCATION}'/g" '''.format(
            SERVER_LOCATION=kwargs['SERVER_LOCATION']
        ), shell_escape=True)"""

        src = "src/server.ts"
        sio = StringIO()
        get(src, sio, use_sudo=True)
        s = sio.read()
        s.replace(
            "app.set('SOCK_URL', undefined);",
            "app.set('SOCK_URL', '{SERVER_LOCATION}');".format(
                SERVER_LOCATION=kwargs["SERVER_LOCATION"]
            ),
        )
        sio = StringIO(s)
        put(sio, src, use_sudo=True)
        run("npm start")


@_validate
def setup_nginx_conf2(*args, **kwargs):
    server_dir = _get_server_dir(**kwargs)
    _setup_nginx_conf2(
        #
        # resource_filename('offregister_nginx', path.join('conf', 'nginx.static.conf'))
        **{
            "nginx-conf-file": path.join(
                get_python_lib(), "offregister_nginx", "conf", "nginx.static.conf"
            ),
            "nginx-conf-filename": kwargs["nginx-conf-filename"],
            "nginx-conf-context": {
                "SERVER_LOCATION": server_dir,
                "SERVER_NAME": kwargs["SERVER_NAME"],
            },
            "GIT_REPO": kwargs["GIT_REPO"],
            "SERVER_LOCATION": server_dir,
            "SERVER_NAME": kwargs["SERVER_NAME"],
        }
    )
