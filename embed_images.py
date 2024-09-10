from helpers import load_images
import os
from multiprocessing import Pool
import torch
from deepface import DeepFace
from torch.nn import DataParallel
import math
import numpy as np

model = 'Facenet512'
model = DataParallel(model)
model.cuda()
batch_size = 10

def embed_batches(image_paths):
    folder = '/home/patrickwilliamson/embeddings'
    for image in image_paths:
        try:
            embedding = DeepFace.represent(img_path=image, model_name="Facenet512", model=model.module)
            base_name = image.split('.')[0].split('/')[-1]
            npy_name = f'{folder}/{base_name}.npy'
            np.save(npy_name, np.array(embedding))
            print(f'saved embedding {npy_name}')
        except Exception as e:
            print(f'error with embedding {e}')
            continue
    print('done with batch')

def main():
    image_paths = load_images('/home/patrickwilliamson/tmp/images')
    chunk_size = 10

    for i in range(0, 100, chunk_size):
        embed_batches(image_paths[i:i+chunk_size]) 
   
if __name__ == '__main__':
    main()
