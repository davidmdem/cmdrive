import yaml
import uuid
from CloudFile import CloudFile
from db.DBProviderABC import DBProviderABC
from os import listdir
from os.path import isfile, join, abspath

class LocalDBProvider(DBProviderABC):
    """
    The local DB provider uses a folder with yaml files representing each cloud resource.
    """

    def __init__(self, db_path):
        """
        Initialize local db provider by scanning for yaml files in in the path
        """
        self.db_path = abspath(db_path)


    def list_files(self):
        """
        Return a list of Cloud Files tracked in this DB
        """
        print("local db list files")
        
        # List of absolute paths for documents representing Cloud Files.
        self.cloud_file_entries = [join(self.db_path, f) for f in listdir(self.db_path) if isfile(join(self.db_path, f))]

        # Converted list of `cloud_file_entries` to list of CloudFile objects.
        return [self.read_file(entry) for entry in self.cloud_file_entries]

    def add(self, local_path):
        """
        Add a new Cloud File to the local DB
        """
        cloud_file = CloudFile().from_local_path(local_path)

        # todo: Should the file name contain a uuid? Or should it be a more exact match of the `name`?
        file_name = cloud_file.name + "_" + str(uuid.uuid4()) + ".yaml"
        file_path = join(self.db_path, file_name)

        cloud_file.url = file_path

        with open(file_path, "w") as output:
            yaml.dump(cloud_file, output)

    def delete(self, cloud_file):
        """
        Remove a CloudFile from the local db
        """
        pass

    def update(self, cloud_file):
        """
        Update an existing Cloud File entry
        """
        pass

    def read_file(self, yaml_file_path):
        """
        Read a yaml file from disk and return the python object it represents.
        """
        obj = {}
        with open(yaml_file_path, "r") as stream:
            try:
                obj = yaml.load(stream)
            except yaml.YAMLError as ex:
                print(ex)    
        return obj
        
