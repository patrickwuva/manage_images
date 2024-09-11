import glob
import os
def main():
    images = glob.glob('/home/patrickwilliamson/tmp/images/*', recursive=True)
    embedded = glob.glob('/home/patrickwilliamson/embedded/*', recursive=True)
    
    images = [i.split('.')[-1] for i in images]
    embedded = [i.split('.')[-1] for i in embedded]
    verified_e = [x for x in images if x in embedded]
    print(len(verified_e))

if __name__ == '__main__':
    main()