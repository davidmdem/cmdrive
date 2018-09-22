
import os
import yaml
from db.DBProviderABC import DBProviderABC

class LocalDBProvider(DBProviderABC):
    """
    The local DB provider uses a folder with yaml files representing each cloud resource.
    """

    def __init__(self, db_path):
        self.db_path = db_path
        print('local db init at ' + self.db_path)
        pass

    def list_files(self):
        print("local db list files")
        pass
        
    def list_dirs(self):
        print("local db list dirs")
        pass
        
    def add(self, cloudFile):
        pass

    def delete(self):
        pass

    def update(self, cloudFile):
        pass

