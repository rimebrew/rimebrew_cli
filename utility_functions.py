import io
import os
import shutil
import tempfile
import typing
import urllib.request
import zipfile
from pathlib import Path

import yaml


# commonly used functions

def mkdir(_path: 'str'):
    Path(_path).mkdir(parents=True, exist_ok=True)


def download_url_to_path(url: str, destination_path: str):
    with urllib.request.urlopen(url) as dl_file:
        with open(destination_path, 'wb') as out_file:
            out_file.write(dl_file.read())


def download_url_to_file(url: str, file: io.TextIOWrapper):
    with urllib.request.urlopen(url) as dl_file:
        file.write(dl_file.read())


def fetch_zip_file_to(url: str, dest_dir: str, folder_name=None):
    mkdir(dest_dir)
    temp = tempfile.TemporaryFile()
    download_url_to_file(url, temp)

    with zipfile.ZipFile(temp, 'r', ) as myzip:
        _main_name = myzip.namelist()[0]
        for file in myzip.namelist():
            if file.startswith(_main_name):
                myzip.extractall(path=dest_dir)
    if folder_name is not None:
        if os.path.exists(dest_dir + '/' + folder_name): shutil.rmtree(dest_dir + '/' + folder_name)
        os.rename(dest_dir + '/' + _main_name, dest_dir + '/' + folder_name)


def load_from_yamlfile(_path: str) -> typing.Union[list, dict]:
    with open(_path, 'r') as yaml_config_file:
        return yaml.load(yaml_config_file, Loader=yaml.Loader)


def load_yaml_doc(_path: str):
    with open(_path, 'r') as file:
        return [document for document in yaml.load_all(file, Loader=yaml.Loader)]


def dump_yaml(_content: str, _path: str):
    with open(_path, 'wb') as _file:
        _file.write(yaml.dump(_content, allow_unicode=True).encode())

# PYTHON

def strJoin(*strings):
    return ''.join(strings)
