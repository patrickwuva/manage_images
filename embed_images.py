import os
import torch
from deepface import DeepFace
import numpy as np
from helpers import load_images

model_name = "Facenet512"
batch_size = 10
num_gpus = torch.cuda.device_count()
total = 0

def embed_batches(image_paths, device_id):
    global total
    folder = '/home/patrickwilliamson/embeddings'
    device = torch.device(f'cuda:{device_id}') 
    for image in image_paths:
        try:
          
            with torch.cuda.device(device_id):
                embedding = DeepFace.represent(img_path=image, model_name=model_name)

           
            base_name = image.split('.')[0].split('/')[-1]
            npy_name = f'{folder}/{base_name}.npy'
            np.save(npy_name, np.array(embedding))
            total +=1
            print(f'done with {total} embeddings')
        except Exception as e:
            print(f'Error with embedding {e} on GPU {device_id}')
            continue


def main():
    image_paths = load_images('/home/patrickwilliamson/tmp/images')
    chunk_size = batch_size * num_gpus 
    total_images = len(image_paths)
    
    for i in range(0, total_images, chunk_size):
        batch = image_paths[i:i + chunk_size] 
        batches_per_gpu = np.array_split(batch, num_gpus) 

        for gpu_id, gpu_batch in enumerate(batches_per_gpu):
            if len(gpu_batch) > 0:
                embed_batches(gpu_batch, gpu_id)

if __name__ == '__main__':
    main()
