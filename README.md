offregister_angular2
====================
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech)
![Python version range](https://img.shields.io/badge/python-2.7%20|%203.5%20|%203.6%20|%203.7%20|%203.8%20|%203.9%20|%203.10%20|%203.11%20|%203.12%20|%203.13-blue.svg)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT%20OR%20CC0--1.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort)

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

Licensed under any of:

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)
- CC0 license ([LICENSE-CC0](LICENSE-CC0) or <https://creativecommons.org/publicdomain/zero/1.0/legalcode>)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
licensed as above, without any additional terms or conditions.
