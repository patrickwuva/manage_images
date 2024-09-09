from helpers import list_files
import deepface
import os

def main():
    image_files = list_files('offender-images')
    print(len(image_files))

if __name__ == '__main__':
    main()
