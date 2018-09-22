import os
from storage.StorageProviderABC import StorageProviderABC

class LocalStorageProvider(StorageProviderABC):
    
    def list_files(self):
        '''
        get a list of stored files
        :return: a list of CloudFiles
        '''
        pass

    def add(self, cloud_file):
        '''
        add a new CloudFile to the database
        
        todo: not sure if this should take a cloud file entry or not. path, policies might be a better choice
        
        :param cloud_file: a CloudFile. todo
        :return: a CloudFile with resource information filled in
        '''
        pass

    def delete(self, cloud_file):
        '''
        delete a file from the database
        :param cloud_file: the cloud file entry being deleted
        '''
        pass

    def update(self, cloud_file):
        '''
        update a file
        :param cloud_file: the cloud file entry being updated
        :return: the updated CloudFile
        '''
        pass
