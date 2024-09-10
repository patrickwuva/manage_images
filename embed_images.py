import os
import torch
from deepface import DeepFace
import numpy as np
from helpers import load_images

# Set the model name and batch size
model_name = "Facenet512"
batch_size = 10
num_gpus = torch.cuda.device_count()  # Automatically get the number of available GPUs

# Function to embed batches and distribute across GPUs
def embed_batches(image_paths, device_id):
    folder = '/home/patrickwilliamson/embeddings'
    device = torch.device(f'cuda:{device_id}')  # Specify the GPU device

    for image in image_paths:
        try:
            # Set the specific device for DeepFace (though DeepFace doesn't directly use this)
            with torch.cuda.device(device_id):
                embedding = DeepFace.represent(img_path=image, model_name=model_name)

            # Save the embedding
            base_name = image.split('.')[0].split('/')[-1]
            npy_name = f'{folder}/{base_name}.npy'
            np.save(npy_name, np.array(embedding))
            print(f'Saved embedding {npy_name} on GPU {device_id}')
        except Exception as e:
            print(f'Error with embedding {e} on GPU {device_id}')
            continue
    print(f'Done with batch on GPU {device_id}')

# Function to distribute image batches across GPUs
def main():
    image_paths = load_images('/home/patrickwilliamson/tmp/images')
    chunk_size = batch_size * num_gpus  # Process a number of batches equal to batch size * number of GPUs
    total_images = len(image_paths)

    # Process images in chunks, distributing batches across GPUs
    for i in range(0, total_images, chunk_size):
        batch = image_paths[i:i + chunk_size]  # Get a chunk of images
        batches_per_gpu = np.array_split(batch, num_gpus)  # Split images into sub-batches for each GPU

        # Create parallel processes for each GPU
        for gpu_id, gpu_batch in enumerate(batches_per_gpu):
            if len(gpu_batch) > 0:
                embed_batches(gpu_batch, gpu_id)  # Assign each sub-batch to a different GPU

if __name__ == '__main__':
    main()
