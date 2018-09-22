import datetime

class CloudFile():
    """
    Model for cloud file database entry.
    """
    def __init__(self):
        self.name = 'test'
        self.owner = 'test-owner'
        self.size = 1024
        self.date_created = datetime.datetime.now()
        self.date_modified = datetime.datetime.now()
        self.date_touched = datetime.datetime.now()
        self.service = 'google'
        self.url = 'https://url.com'
        self.policies = [
            'all'
        ]
        
    def from_local_path(self, path):
        pass

    def from_obj(self, obj):
        pass
        