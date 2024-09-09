import os

def list_files(bucket_name):
    files = []
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    for blob in blobs:
        files.append(blob.name)
   return files

def download_files(bucket_name, file_list):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    os.makedirs('/home/patrickwilliamson/images', exist_ok=True)

    for i, file_name in enumerate(file_list[:limit]):
        blob = bucket.blob(file_name)
        destination_file_path = os.path.join('/home/patrickwilliamson/images', file_name)
        os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)

        blob.download_to_filename(destination_file_path)
