offregister_angular2
====================
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech)
![Python version range](https://img.shields.io/badge/python-2.7%20|%203.4%20|%203.5%20|%203.6%20|%203.7%20|%203.8-blue.svg)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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

## License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.
