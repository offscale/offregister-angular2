offregister_angular2
====================
This package follows the [offregister](https://github.com/offscale/offregister) specification to setup and serve a static application.

It deploys some static files (like an Angular2 app), and a Node.JS server for prerendering.

## Install dependencies

    pip install -r requirements.txt

## Install package

    pip install .

## Configuration options

### `SERVER_LOCATION`
###### Default: `/var/www/static/${NAME_OF_BLOCK:-'git-repo'}`
Where to clone the files. Defaults where `git-repo` is the last bit of `GIT_REPO` (without the `.git`).
 
### `GIT_REPO`
Where the static files are located, e.g.: `https://github.com/org/git-repo.git ` 
    
### `SERVER_LOCATION`
Where to run the server, e.g.: `unix:/run/my-server.sock` or `http://0.0.0.0:8080`
