import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', type=str)

def main(args):
    os.system(f'python DeepMLS_Generation.py --i {args.i}')
    os.system(f'python mls_marching_cubes.py --i {args.i}')
    

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)