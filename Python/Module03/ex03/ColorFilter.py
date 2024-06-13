import numpy as np
from ImageProcessor import ImageProcessor

class ColorFilter:

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        # array is a broadcasted numpy with normalized values (between 0 and 1)
        # so subtracting from 1 will flip the intensity values and invert the image
        inverted = 1 - array

        # in image processing, each pixel often contains 4 channels of data RGBA
        # RGB = RGB Channels representing the red, green and blue color components
        # A = Alpha Channel determining the transparency and opacity of each pixel
        # here, we want to slice across all dimension of the array (...) 
        # starting from the 4th channel Alpha
        # this line ensures that after inverting, the original Alpha channel remains unchanged
        inverted[..., 3:] = array[..., 3:]
        return inverted.astype(array.dtype)


    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        blue_array = array.copy()
        # sets the Red channel to 0
        blue_array[:, :, 0] = 0
        # sets the Green channel to 0
        blue_array[:, :, 1] = 0
        return blue_array


    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        green_array = array.copy()
        # sets the Red channel to 0
        green_array[:, :, 0] = 0
        # sets the Blue channel to 0
        green_array[:, :, 2] = 0
        return green_array


    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        red_array = array.copy()
        # sets the Green channel to 0
        red_array[:, :, 1] = 0
        # sets the Blue channel to 0
        red_array[:, :, 2] = 0
        return red_array


    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        array_copy = array.copy()
        # linspace(start, stop, num) returns num evenly spaced samples, calculated over the interval [start, stop]
        # linspace(2.0, 3.0, num=5) => array([2.  , 2.25, 2.5 , 2.75, 3.  ])
        thresholds = np.linspace(array_copy.min(), array_copy.max(), num=5)
        for i in range(len(thresholds) - 1):
            # sets all pixel values in array_copy that fall within the range 
            # defined by thresholds[i] and thresholds[i + 1] to thresholds[i]
            array_copy[(array_copy >= thresholds[i]) & (array_copy <= thresholds[i + 1])] = thresholds[i]
        return array_copy


    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if filter in ['m', 'mean']:
            # computes the mean of the RGB channels across the third axis=2
            # this results in a grayscale image where each pixel is the average of its RGB components
            gray_array = np.mean(array, axis=2, dtype=array.dtype)
        elif filter in ['w', 'weight']:
            weights = kwargs.get('weights')

            # checks if weights is a list of 3 floats that sums up to 1
            if weights is None or len(weights) != 3 or not np.isclose(sum(weights), 1.0):
                return None
            
            # apply weights to RGB channels with dot (matrix multiplication)
            gray_array = np.dot(array[..., :3], weights)
        else:
            return None
        return gray_array.astype(array.dtype)
        

imp = ImageProcessor()
arr = imp.load("../resources/Elon.png")

cf = ColorFilter()
imp.display(cf.invert(arr))
imp.display(cf.to_green(arr))
imp.display(cf.to_red(arr))
imp.display(cf.to_blue(arr))
imp.display(cf.to_celluloid(arr))
imp.display(cf.to_grayscale(arr, 'm'))
imp.display(cf.to_grayscale(arr, 'weight', weights = [0.2, 0.3, 0.5]))
