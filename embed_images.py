import os
from multiprocessing import Pool

def embed_chunk_on_gpu(image_paths, gpu_id):
    os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)
    
    from deepface import DeepFace
    import numpy as np

    for image in image_paths:
        try:
            embedded_image = np.array(DeepFace.represent(
                img_path=image,
                model_name='Facenet512'
            ))
            output = image.split('.')[0].split('/')[-1]
            np.save(f'/path/to/output/{output}.npy', embedded_image)
            print(f'Embedded {image} on GPU {gpu_id}')
        except Exception as e:
            print(f'Error embedding image {image} on GPU {gpu_id}: {e}')

def main():
    image_paths = load_images('/home/patrickwilliamson/tmp/images')
    chunk_size = 25
    
    chunks = [image_paths[i:i + chunk_size] for i in range(0, len(image_paths), chunk_size)]
    
    with Pool(processes=4) as pool:  # Assuming 4 GPUs
        pool.starmap(embed_chunk_on_gpu, [(chunk, i % 4) for i, chunk in enumerate(chunks)])

if __name__ == '__main__':
    main()
