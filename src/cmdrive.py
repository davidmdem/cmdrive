"""Cloudmesh Drive.

Usage:
  cmdrive.py add FILE
  cmdrive.py add SERVICE FILE 
  cmdrive.py get FILE
  cmdrive.py get FILE DEST_FOLDER
  cmdrive.py del FILE
  cmdrive.py (ls | dir)
  cmdrive.py (-h | --help)
  cmdrive.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --config      Location of a cmdrive.yaml file
"""

import os
import yaml
from docopt import docopt
from CloudFile import CloudFile
from db.LocalDBProvider import LocalDBProvider
from storage.LocalStorageProvider import LocalStorageProvider

class cmdrive:

    def __init__(self):
        self._db = None
        self._conf = {}
        self._providers = {}

    def config(self, config_path='./cmdrive.yaml'):
        ''' 
        Use `cmdrvie.yaml` and environ vars to configure.
        '''
        # Read config file
        with open(config_path, "r") as stream:
            conf = yaml.load(stream)
            self._conf = conf.get('cmdrive')

        # Set DB provider. There should only be one.
        db_provider = self._conf.get('default').get('db')

        if db_provider == 'local':
            db_path =  self._conf.get('db').get('local').get('CMDRIVE_DB_FOLDER') or os.environ.get('CMDRIVE_DB_FOLDER')
            self._db = LocalDBProvider(db_path)

        # Set storage providers. Can be many.
        storage_path = self._conf.get('service').get('local').get('CMDRIVE_STORAGE_FOLDER') or os.environ.get('CMDRIVE_STORAGE_FOLDER')
        if storage_path:
            self._providers['local'] = LocalStorageProvider(storage_path)

        # Set a the default storage provider.
        default_storage_provider = self._conf.get('default').get('service')
        self._providers['default'] = self._providers[default_storage_provider]

    def ls(self):
        '''
        List tracked files.
        '''
        self._print_row("FILE", "URL", "SERVICE", "SIZE")
        for f in self._db.list_files():
            self._print_row(f.name, f.url, f.service, f.size)

    def add(self, provider, file_path):
        '''
        Add a new file

        :param provider: The storage provider where the file should be stored.
        :param file_path: The local path to the file.
        '''
        new_cloud_file = self._providers[provider or 'default'].add(file_path)
        self._db.add(new_cloud_file)

    def get(self, file_name, dest_folder='.'):
        '''
        Retrieve a file

        :param file_name: The name corresponding to the cloud file to be downloaded.
        '''
        # Get db entry for this file
        cloud_file = self._db.get(file_name)

        if not cloud_file:
            print("Requested file not found. Use `ls` to see a list of file names.")
            raise SystemExit

        # Todo: docopt default for this?
        dest_folder = dest_folder or '.'
        self._providers[cloud_file.service].get(cloud_file, dest_folder)
    
    def delete(self, file_name):
        '''
        Remove a file
        :param file_name: The name of the file to remove.
        '''
        cloud_file = self._db.get(file_name)
        self._providers[cloud_file.service].delete(cloud_file)
        self._db.delete(cloud_file)
        
    def _print_row(self, file_name, url, service, size):
        '''
        Print a formatted row
        '''
        print(" %-35s %-50s %-10s %-10s" % (file_name, url, service, size))


if __name__ == "__main__":
    arguments = docopt(__doc__, version='Cloudmesh Drive 0.1')

    cd = cmdrive()
    cd.config() 

    if arguments['ls'] or arguments['dir']:
        cd.ls()
    elif arguments['add'] and arguments['FILE']:
        cd.add(arguments['SERVICE'], arguments['FILE'])
    elif arguments['del'] and arguments['FILE']:
        cd.delete(arguments['FILE'])
    elif arguments['get'] and arguments['FILE']:
        cd.get(arguments['FILE'], arguments['DEST_FOLDER'])

