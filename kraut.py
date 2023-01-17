"""Compressed Pickler: kraut"""

__version__ = "0.1"

import bz2
import os
import pickle


def write_compressed(file_path, data):
    file_dir = os.path.dirname(file_path)

    if file_dir and not os.path.exists(file_dir):
        os.makedirs(file_dir)

    with bz2.open(file_path, "wb") as f:
        pickle.dump(data, f)


def read_compressed(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    with bz2.open(file_path, "rb") as f:
        data = pickle.load(f)
    return data
