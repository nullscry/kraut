# kraut

[![Build Status](https://github.com/nullscry/dupe-be-gone/actions/workflows/ci.yml/badge.svg)](https://github.com/nullscry/dupe-be-gone/actions/workflows/ci.yml)
[![Release Status](https://github.com/nullscry/dupe-be-gone/actions/workflows/release.yml/badge.svg)](https://github.com/nullscry/dupe-be-gone/releases)
[![Crate Status](https://img.shields.io/crates/v/dupe-be-gone.svg)](https://crates.io/crates/dupe-be-gone)
[![Docs Status](https://docs.rs/dupe-be-gone/badge.svg)](https://docs.rs/crate/dupe-be-gone/)

`pickle` with built in compression with Python Standard Library `bz2` with no dependencies. Useful for serializing massive Dict objects, CSV files or NetworkX graphs and many more.

## Installation

```sh
pip install kraut
```

## Usage

```python
from kraut import write_compressed, read_compressed
my_huge_data_object = {...}

write_compressed("save/myobj.pkl.bz2", my_huge_data_object):

...

my_restored_object =  read_compressed("save/myobj.pkl.bz2"):

assertEqual(my_huge_data_object, my_restored_object)
```
