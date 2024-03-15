from google.cloud import storage

def create_bucket(bucket_name):
    """Creates a new bucket."""
    # TODO: Replace 'your-project-id' with your actual project ID
    storage_client = storage.Client('dev-env-1-412811')

    bucket = storage_client.create_bucket(bucket_name)

    print('Bucket {} created'.format(bucket.name))

create_bucket('my-bucket')
