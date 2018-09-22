import yaml
from db.DBProviderABC import DBProviderABC
from os import listdir
from os.path import isfile, join, abspath

class LocalDBProvider(DBProviderABC):
    """
    The local DB provider uses a folder with yaml files representing each cloud resource.
    """

    def __init__(self, db_path):
        self.db_path = abspath(db_path)

        #todo: serialize files into collection
        self.cloud_file_entries = [f for f in listdir(self.db_path) if isfile(join(self.db_path, f))]

    def list_files(self):
        print("local db list files")
        return self.cloud_files
        
    def list_dirs(self):
        print("local db list dirs")
        pass
        
    def add(self, cloud_file):
        print("localdb add cloud file entry")

        with open(self.db_path + cloud_file.name, "w") as output:
            yaml.dump(cloud_file, output)

    def delete(self):
        pass

    def update(self, cloudFile):
        pass

