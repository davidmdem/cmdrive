"""Cloudmesh Drive.

Usage:
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

def main():
    arguments = docopt(__doc__, version='Cloudmesh Drive 0.1')
    
    print("Enter main")
    db_path = os.environ.get('CMDRIVE_DB_FOLDER') or ''

    localdb = LocalDBProvider(db_path)
    local_files = localdb.list_files()
    local_dirs = localdb.list_dirs()
    print("done")

if __name__ == "__main__":
    main()
