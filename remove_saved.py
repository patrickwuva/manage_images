import glob
import os
def main():
    images = glob.glob('/home/patrickwilliamson/tmp/images/*')
    embedded = glob.glob('/home/patrickwilliamson/embeddings/*')
    
    images = [i.split('.')[0].split('/')[-1] for i in images]
    embedded = [i.split('.')[0].split('/')[-1] for i in embedded]
    print(images[0])
    print(embedded[0])
    verified_e = [x for x in images if x in embedded]
    print(len(verified_e))

if __name__ == '__main__':
    main()