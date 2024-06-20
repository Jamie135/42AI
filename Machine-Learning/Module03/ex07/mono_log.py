import argparse
import pandas
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-zipcode", type=int, choices=(0, 1, 2, 3), required=True)
        args = parser.parse_args()
        zipcode = args.zipcode
    except argparse.ArgumentError:
        print("Usage: --zipcode must be 0, 1, 2, or 3")