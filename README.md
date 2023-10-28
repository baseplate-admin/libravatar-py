# A libravatar client for Python thats built on modern Technology

[![Pepy.tech Badge](https://static.pepy.tech/personalized-badge/libravatar-py?period=week&units=international_system&left_color=grey&right_color=orange&left_text=Downloads)](https://pepy.tech/project/libravatar-py)
[![PyPi Version Badge](https://badge.fury.io/py/libravatar-py.svg)](https://badge.fury.io/py/libravatar-py)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/libravatar-py)](https://github.com/baseplate-admin/libravatar-py/blob/main/setup.py)
[![PyPI - License](https://img.shields.io/pypi/l/libravatar-py)](https://github.com/baseplate-admin/libravatar-py/blob/main/LICENSE)
![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)
[![Lines of Code](https://tokei.rs/b1/github/baseplate-admin/libravatar-py)](https://github.com/baseplate-admin/libravatar-py)

## Introduction :

Friendly fork of [pyLibravatar](https://launchpad.net/pylibravatar).

### Why did I write this library:

While working on the Libravatar client project I came across the well built [pyLibravatar](https://pypi.org/project/pyLibravatar) library. The last update was at Jun 28, 2015 ( Thats over 6 years ago when I was writing this ). So thats why I decided to write this library. It mimics the API ( and functionality ) of [pyLibravatar](https://pypi.org/project/pyLibravatar) but with `asyncio` spice.

### Why use \"libravatar-py\" ?

-   Provides API for different kinds of usage.
-   Built with modern techknology.
-   No unnecessary codes. ( My goal was to keep the library as small as
    possible )
-   Is very minimal. ( Only provides 4 functions )
-   Fully Fedarated and feature rich.

### Why shouldn\'t you use \"libravatar-py\" ?

-   I donno ? If you do please submit a Pull Request

# User guide :

## Installation :

Install with pip from pypi (No extra dependencies):

```bash
$ python -m pip install libravatar-py
```

Install with pip from github ( Development | Not Recommended for Production ):
```bash
$ python -m pip install https://codeload.github.com/baseplate-admin/libravatar-py/zip/refs/heads/main
```
## Usage:

Call any of these 4 methods.

`libravatar_url` function ( This will essentially return the base url of
the image ) :

```python
from libravatar import libravatar_url

url = libravatar_url(email="someone@example.com")
print(url)
# https://seccdn.libravatar.org/avatar/16d113840f999444259f73bac9ab8b10
```

`libravatar_img_tag` function ( This will wrap the libravatar url in a \<img /\> tag. You can also customize \_alt text ) :

```python
from libravatar import libravatar_img_tag

url = libravatar_img_tag(email="someone@example.com")
print(url)
# <img src=https://seccdn.libravatar.org/avatar/16d113840f999444259f73bac9ab8b10 alt='Avatar for someone@example.com' />
```

`libravatar_raw_image` function ( This will return the Libravatar image in a binary form ) :

``` python
from libravatar import libravatar_raw_image

res = libravatar_raw_image(email="someone@example.com")
print(res)
# Large binary string.
# To load it.
from PIL import Image
from io import BytesIO

res = Image.open(BytesIO(res))
```

`libravatar_raw_query` function ( Essentially passes the {args, kwargs} to httpx_get_avatar ):

``` python
from libravatar import libravatar_raw_image
# Note this this must be called from an async function
res = await libravatar_raw_query(email="someone@example.com", {})
# All httpx variables available in res
```

# Contributing :

If you like this project add a star. If you have problems or suggestions please put them in the [Issue Tracker](https://github.com/baseplate-admin/libravatar-py/issues). If
you like to add features. Fork this repo and submit a Pull Request. 😛

# Updates :

The library is feature complete ( in my opinion ).
