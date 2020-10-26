import configparser
import pathlib
from pyzotero import zotero

from .auth import parse_auth_from_ini, get_auth_from_pkg_ini

# Load API params for  authentication
config = configparser.ConfigParser()
config.read('zotero.ini')
config_filepath_tmp = config['Default']['config_filepath']
config_filepath = pathlib.Path(config_filepath_tmp).expanduser()
if not config_filepath.exists():
    raise ValueError(f"config_filepath {config_filepath} not a file")
config.read(config_filepath)
library_id = config['Default']['library_id']
library_type = config['Default']['library_type']
api_key = config['Default']['api_key']

# Connection object
zot = zotero.Zotero(library_id, library_type, api_key)

if __name__ == '__main__':

    print('library_id : ', library_id)
    print('library_type : ', library_type)
    print('api_key : ', api_key)

    print('Test Connection....')
    print('Total number of items: ', zot.count_items())
    items = zot.top(limit=5)
    # we've retrieved the latest five top-level items in our library
    # we can print each item's item type and ID
    for item in items:
        print('Item Type: %s | Key: %s | Title: %s' \
            % (item['data']['itemType'], item['data']['key'],
                item['data']['title']))
