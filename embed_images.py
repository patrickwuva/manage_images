from helpers import list_files, download_files, save_progress, get_progess, load_images, embed_image
from concurrent.futures import ThreadPoolExecutor
import os

def embed_chunk(image_paths, index):
    for image in image_paths:
        #download_files('offender-images', image_paths)
        embed_image(image)
    save_progress(index)
    print(f'done with chunk {index}')
        
def main():
    image_paths = load_images('/home/patrickwilliamson/tmp/images')
    chunk_size = 25
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(embed_chunk, image_paths[i:i+chunk_size], i//chunk_size) for i in range(0, 5000, chunk_size)]

        for future in futures:
            print(future.result())

if __name__ == '__main__':
    main()
