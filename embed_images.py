from helpers import list_files, download_files, save_progress, get_progess, load_images
import deepface
import os

def main():

    image_paths = load_images()
    print(len(image_paths))

if __name__ == '__main__':
    main()
