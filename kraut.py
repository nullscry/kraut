"""Compressed Pickler: kraut"""

__version__ = "0.2"

import bz2
import os
import pickle


def write_compressed(file_path, data):
    """
    Compress `data` with bz2 compression and serialize
    using pickle at `file_path`. Also create missing directories.

    Args:
        `file_path`: Absolute or Relative destination path
        `data`: Any object that can be safely pickled
    """
    file_dir = os.path.dirname(file_path)

    if file_dir and not os.path.exists(file_dir):
        os.makedirs(file_dir)

    with bz2.open(file_path, "wb") as f:
        pickle.dump(data, f)


def read_compressed(file_path):
    """
    Read data serialized with `kraut.write_compressed`
    at `file_path`.

    Args:
        `file_path`: Absolute or Relative target path

    Returns:
        data contained at `file_path`

    Raises:
        `FileNotFoundError`: If `file_path` does not exist
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    with bz2.open(file_path, "rb") as f:
        data = pickle.load(f)
    return data
