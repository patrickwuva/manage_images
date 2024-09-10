from helpers import list_files, download_files, save_progress, get_progess, load_images, embed_image
from multiprocessing import Pool
import os

def embed_chunk(image_paths):
    for image in image_paths:
        embed_image(image)
    
    print(f'done with chunk containing {len(image_paths)} images')

def main():
    image_paths = load_images('/home/patrickwilliamson/tmp/images')
    chunk_size = 25

    chunks = [image_paths[i:i + chunk_size] for i in range(0, len(image_paths), chunk_size)]

    with Pool(processes=3) as pool:
        pool.map(embed_chunk, chunks)

if __name__ == '__main__':
    main()
