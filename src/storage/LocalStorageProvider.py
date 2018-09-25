import os
import yaml
import shutil
from pathlib import Path
from os.path import abspath
from CloudFile import CloudFile
from storage.StorageProviderABC import StorageProviderABC

class LocalStorageProvider(StorageProviderABC):
    
    def __init__(self, storage_path):
        '''
        Initialize storage path
        '''
        self._path = Path(storage_path)

    def add(self, local_path):
        '''
        add a new CloudFile to the database
        
        :param local_path: Path to a file that will be stored.
        :return: a CloudFile with resource information filled in
        '''
        local_path = abspath(local_path)

        cloud_file = CloudFile().from_local_path(local_path)
        cloud_file.url = abspath(self._path.joinpath(cloud_file.name))
        cloud_file.service = 'local'

        shutil.copy(local_path, cloud_file.url)
        return cloud_file

    def get(self, cloud_file, local_dest):
        '''
        Download the file from the `cloud_file.url` to a local folder.

        :param cloud_file: A cloud file entry from the db. 
        :param local_dest: A local path where the cloud file will be downloaded.
        '''
        local_dest = Path(local_dest)
        shutil.copy(cloud_file.url, local_dest.joinpath(cloud_file.name))

    def delete(self, cloud_file):
        '''
        delete a file from the database

        :param cloud_file: the cloud file entry being deleted
        '''
        os.remove(cloud_file.url)
