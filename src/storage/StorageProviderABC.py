import abc

class StorageProviderABC(metaclass = abc.ABCMeta):
    """
    Abstract Base Class for supported cloud providers.
    """

    @abc.abstractmethod
    def get(self, cloud_file):
        '''
        get a file stored with this provider
        :param cloud_file: the cloud file entry being retrieved
        :return: the downloaded cloud file binary
        '''
        pass

    @abc.abstractmethod
    def add(self, cloud_file):
        '''
        upload a file
        
        todo: not sure if this should take a cloud file entry or not. (path, policies) might be a better choice
        
        :param cloud_file: a CloudFile. todo
        :return: a CloudFile with resource information filled in
        '''
        pass

    @abc.abstractmethod
    def delete(self, cloud_file):
        '''
        delete a file from the provider
        :param cloud_file: the cloud file entry being deleted
        '''
        pass

    @abc.abstractmethod
    def update(self, cloud_file):
        '''
        update a file
        :param cloud_file: the cloud file entry being retrieved
        :return: the downloaded cloud file binary
        '''
        pass

    @abc.abstractmethod
    def list_files(self, dir):
        '''
        get a list of files stored in a directory
        :return: a list of CloudFiles
        '''
        pass

    @abc.abstractmethod
    def list_dirs(self):
        '''
        get a list of directories in this provider
        :return: a list of CloudFiles
        '''
        pass
