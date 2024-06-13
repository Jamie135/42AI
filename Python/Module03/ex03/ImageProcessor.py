import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

class ImageProcessor:

    def load(self, path):
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"FileNotFoundError: No such file or directory")
            
            # context manager to help close file in case of error
            with Image.open(path) as img:
                # use array() to convert the img object into array of float32
                img_array = np.array(img).astype(np.float32) / 255.0
                print(f"Loading image of dimensions {img_array.shape[0]} x {img_array.shape[1]}")
                return img_array

        except FileNotFoundError as fnferr:
            print(fnferr)
            return None
        except OSError as oserr:
            print(f"OSError: {oserr}")
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


# # Example usage:
# imp = ImageProcessor()
# arr = imp.load("../resources/non_existing_file.png")
# print(arr)
# arr = imp.load("../resources/empty_file.png")
# print(arr)
# arr = imp.load("../resources/42AI.png")
# print(arr)
# imp.display(arr)
