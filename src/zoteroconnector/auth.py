import configparser
import pathlib
import pyzotero
import importlib.resources as resources
from . import config as config_files

ini_format = "[Default]"\
             "library_id : 8192938"\
             "library_type : user"\
             "api_key : safjspoia023uskjdafs"\

def parse_auth_from_ini(config_fpath : pathlib.Path):
    """Parse auth information from ini file"""
    config = configparser.ConfigParser()
    config.read(config_fpath)

    try:
        return dict(library_id = config['Default']['library_id'],
                    library_type = config['Default']['library_type'],
                    api_key = config['Default']['api_key'])
    except: 
        raise KeyError("ini file does not conform to the required format\n" \
                       + ini_format)

def get_auth_from_pkg_ini():
    """Automatically load auth detail with pkg ini file"""

    with resources.path(config_files, "zotero.ini") as pkg_config_path:
        config = configparser.ConfigParser()
        config.read(pkg_config_path)
        config_filepath_tmp = config['Default']['config_filepath']
        config_filepath = pathlib.Path(config_filepath_tmp).expanduser()
        if not config_filepath.exists():
            raise KeyError(f"config_filepath {config_filepath} not a file")
        return parse_auth_from_ini(config_filepath)

if __name__ == "__main__" : 
    pass
