import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

class ImageProcessor:

    def load(self, path):
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Exception: FileNotFoundError -- strerror: No such file or directory")
            
            # context manager to help close file in case of error
            with Image.open(path) as img:
                # use array() to convert the img object into an array of float32
                # use / 255.0 to convert rgb value to normalized value (between 0 and 1)
                img_array = np.array(img).astype(np.float32) / 255.0
                # np.set_printoptions(precision=5, threshold=np.inf, suppress=True)
                print(img_array)
                print(f"Loading image of dimensions {img_array.shape[0]} x {img_array.shape[1]}")
                return img_array

        except FileNotFoundError as fnferr:
            print(fnferr)
            return None
        except OSError as oserr:
            print(f"Exception: OSError -- strerror: None")
            return None
    

    def display(self, array):
        if array is None:
            print("No image to display")
            return
        # prepare the image using numpy array, interpreting the values as pixel and renders the corresponding image
        plt.imshow(array)
        # hide the axis that shows scales and coordinates
        plt.axis('off')
        # renders the image and opens the Matplotlib viewer
        plt.show()


# Example usage:
imp = ImageProcessor()
arr = imp.load("../resources/non_existing_file.png")
print(arr)
arr = imp.load("../resources/empty_file.png")
print(arr)
arr = imp.load("../resources/42AI.png")
imp.display(arr)
