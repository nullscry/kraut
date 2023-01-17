import os
import shutil

import pytest

import kraut

TEST_DIR = "var"
TEST_DICT = {"Test": 0, "Me": 1}


def test_write():
    file_path = os.path.join(TEST_DIR, "TEST_DICT.pkl.bz2")
    kraut.write_compressed(file_path, TEST_DICT)
    assert os.path.exists(file_path)


def test_read_type():
    file_path = os.path.join(TEST_DIR, "TEST_DICT.pkl.bz2")
    kraut.write_compressed(file_path, TEST_DICT)
    read_content = kraut.read_compressed(file_path)
    assert isinstance(read_content, dict)


def test_read_content():
    file_path = os.path.join(TEST_DIR, "TEST_DICT.pkl.bz2")
    kraut.write_compressed(file_path, TEST_DICT)
    read_content = kraut.read_compressed(file_path)
    assert TEST_DICT == read_content


def test_file_not_exist():
    file_path = "IAmDefinitelyNotHere"
    with pytest.raises(FileNotFoundError):
        read_content = kraut.read_compressed(file_path)  # noqa: F841


@pytest.fixture(autouse=True)
def test_folder_fixture():
    if not os.path.exists(TEST_DIR):
        os.makedirs(TEST_DIR)
    yield
    shutil.rmtree(TEST_DIR)
