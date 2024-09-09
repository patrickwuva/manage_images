from helpers import list_files, download_files, save_progress, get_progess
import deepface
import os

def main():

    image_files = list_files('offender-images')
    print(get_progess())

if __name__ == '__main__':
    main()
