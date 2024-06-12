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
        return 255 - array.copy()


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
        blue_array[:, :, 0] = 0
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
        return array * np.array([0, 1, 0])


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
        green_blue = self.to_green(array) + self.to_blue(array)
        return array - green_blue


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
        thresholds = np.linspace(0, 255, 5)
        return np.digitize(array, thresholds) * (255 / 4)


    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
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
            return np.mean(array, axis=-1)
        elif filter in ['w', 'weight']:
            weights = kwargs.get('weights', [0.333, 0.333, 0.333])
            weights = np.array(weights)
            return np.dot(array, weights)
        

imp = ImageProcessor()
arr = imp.load("42AI.png")
# Output :
# Loading image of dimensions 200 x 200

cf = ColorFilter()
imp.display(cf.invert(arr))
imp.display(cf.to_green(arr))
imp.display(cf.to_red(arr))
imp.display(cf.to_blue(arr))
imp.display(cf.to_celluloid(arr))
imp.display(cf.to_grayscale(arr, 'm'))
imp.display(cf.to_grayscale(arr, 'weight', weights = [0.2, 0.3, 0.5]))
