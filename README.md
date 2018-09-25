Cloudmesh Drive
===

## Database Providers

A central database provider keeps track of files stored throughout multiple clouds.

### Local

The [`LocalDBProvider`](src/db/LocalDBProvider.py) uses a folder on the local file system or network share to store each cloud file entry as a yaml file.


### MongoDB

Todo


## Storage Providers

Storage providers are services that allow storing files.

### Local

The [`LocalStorageProvider`](src/storage/LocalStorageProvider.py) uses a folder on the local file system or network share to act as a "cloud" storage provider.

### Azure Blob Storage

See Libcloud's [Azure Blobs Storage Driver Documentation](https://libcloud.readthedocs.io/en/latest/storage/drivers/azure_blobs.html) for instructions on how to setup a storage account and generate access keys.

### Google Cloud Storage

See Libcloud's [Google Storage Driver Documentation](https://libcloud.readthedocs.io/en/latest/storage/drivers/google_storage.html) for instructions on how to setup a storage account and generate access keys.

## Run

The default [`cmdrive.yaml`](src/cmdrive.yaml) is setup to use a local database and storage provider. 

## TODO

- [ ] Get more clarity on command line api
- [ ] See what to do about policies
- [ ] Consider merging the db and cloud provider base classes
- [ ] MongoDB database provider
- [ ] Google Drive integration
- [ ] Box integration
- [ ] AWS integration
- [ ] Command line option for cmdrive.yaml path

