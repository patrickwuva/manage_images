import os
from google.cloud import storage

def list_files(bucket_name):
    files = []
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    for blob in blobs:
        files.append(blob.name)
    
    return files

def download_files(bucket_name, file_list):
    destination_foler = 'home/patrickwilliamson/images'
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    for file in file_list:
        blob = bucket.blob(file)
        blob.download_to_filename(file)

def save_progress(chunk_index):
    with open('/home/patrickwilliamson/progress.txt', 'w') as file:
        file.write(chunk_index)

def get_progess():
    with open('/home/patrickwilliamson/progress.txt', 'r') as file:
        chunk = file.read()
        if chunk is None or chunk == '-1':
            return 0
        else:
            return int(chunk)