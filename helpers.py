import os
from google.cloud import storage
import pickle
from deepface import DeepFace
import numpy as np
import glob

def list_files(bucket_name):
    files = []
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    for blob in blobs:
        files.append(blob.name)
    
    return files

def download_files(bucket_name, file_list):
    destination_foler = '/home/patrickwilliamson/images'
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    for file in file_list:
        blob = bucket.blob(file)
        blob.download_to_filename(f'/home/patrickwilliamson/{file}')

def save_progress(chunk_index):
    with open('/home/patrickwilliamson/progress.txt', 'w') as file:
        file.write(str(chunk_index))

def get_progess():
    with open('/home/patrickwilliamson/progress.txt', 'r') as file:
        chunk = file.read()
        if chunk is None or chunk == '-1':
            return 0
        else:
            return int(chunk)
        
def load_images(folder_path=None):
    if folder_path:
        images = []
        for file in glob.glob(f'{folder_path}/*'):
            images.append(file)
        return images
    
    with open('/home/patrickwilliamson/image_paths.pkl', 'rb') as f:
        return pickle.load(f)

def embed_image(file, output_folder=''):
    try:
        img_path = file
        if output_folder != '':
            img_path = f'/home/patrickwilliamson/{file}'
        embedded_image = np.array(DeepFace.represent(
            
            img_path = img_path,
            model_name = 'Facenet512'
        ))
        output = file.split('.')[0].split('/')[-1]
        np.save(f'{output_folder}{output}.npy', embedded_image)
        print(f'embedded {file}')
    except Exception as e:
        print(f'error while embedding image: {e}')
    finally:
        os.remove(f'{file}')