import glob
import os
def main():
    images = glob.glob('/home/patrickwilliamson/tmp/images/*')
    embedded = glob.glob('/home/patrickwilliamson/embeddings/*')
    
    ending = images[0].split('.')[-1]
    images = [i.split('.')[0].split('/')[-1] for i in images]
    print(embedded[0])
    embedded = [i.split('.')[0].split('/')[-1] for i in embedded]
    verified_e = [x for x in images if x in embedded]
    print(len(verified_e))

    for file in verified_e:
        os.remove(f'{file}.{ending}')
        
if __name__ == '__main__':
    main()