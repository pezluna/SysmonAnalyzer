import sys
import os

import argparse

from src.dataset_refiner import lmd_refiner as lmd_refiner
from src.dataset_refiner import aau_refiner as aau_refiner

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", type=int, required=False, default=0, help="Type of dataset to refine\n0: Both\n1: LMD\n2: AAU")
    args = parser.parse_args()

    if args.type == 0:
        lmd_refiner.refine()
        aau_refiner.refine()
    elif args.type == 1:
        lmd_refiner.refine()
    elif args.type == 2:
        aau_refiner.refine()
    else:
        print("Invalid type")
        sys.exit(1)