"""Cloudmesh Drive.

Usage:
  cmdrive.py add <service> <file>
  cmdrive.py add <file>
  cmdrive.py (ls | dir)
  cmdrive.py (-h | --help)
  cmdrive.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

import os
from docopt import docopt
from CloudFile import CloudFile
from db.LocalDBProvider import LocalDBProvider
from storage.LocalStorageProvider import LocalStorageProvider

config = {}
db_provider = None
service_providers = {}

def main():
    global config
    global db_provider
    global service_providers

    arguments = docopt(__doc__, version='Cloudmesh Drive 0.1')

    db_path = os.environ.get('CMDRIVE_DB_FOLDER') or ''
    db_provider = LocalDBProvider(db_path)

    storage_path = os.environ.get('CMDRIVE_STORAGE_FOLDER') or ''
    service_providers['local'] = LocalStorageProvider(storage_path)

    print("main")
    print(arguments)

    if arguments['ls'] or arguments['dir']:
      ls()

    print("done")

def ls():
    """
    List tracked files
    """
    print(db_provider.list_files())

def add(file_path):
    db_provider.add(file_path)  

def get(file_path):
    pass

if __name__ == "__main__":
    main()
