import numpy as np

class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combination of parameters not compatible).
        
        Raise:
        ------
        This function should not raise any Exception.
        """
        try:
            height, width = dim
            start_y, start_x = position
            return array[start_y:start_y + height, start_x:start_x + width]
        except:
            return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combination of parameters not compatible).
        
        Raise:
        ------
        This function should not raise any Exception.
        """
        # delete(arr, obj, axis=None) returns a new array with sub-arrays along an axis deleted
        # for a one dimensional array, this returns those entries not returned by arr[obj]
        try:
            if axis == 0:
                return np.delete(array, np.s_[n-1::n], axis=0)
            elif axis == 1:
                return np.delete(array, np.s_[n-1::n], axis=1)
        except:
            return None

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combination of parameters not compatible).
        
        Raises:
        -------
        This function should not raise any Exception.
        """
        # concatenate((a1, a2, ...), axis=0, ...) joins a sequence of arrays along an existing axis
        try:
            return np.concatenate([array] * n, axis=axis)
        except:
            return None

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combination of parameters not compatible).
        
        Raises:
        -------
        This function should not raise any Exception.
        """
        # tile(A, reps) constructs an array by repeating A the number of times given by reps
        try:
            return np.tile(array, dim)
        except:
            return None

        

spb = ScrapBooker()

# Example for crop
arr1 = np.arange(0, 25).reshape(5, 5)
print(spb.crop(arr1, (3, 1), (1, 0)))
# Output:
# array([[ 5],
#        [10],
#        [15]])

# Example for thin
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
print(spb.thin(arr2, 3, 0))
# Output:
# array([['A', 'B', 'D', 'E', 'G', 'H', 'J', 'K'],
#        ['A', 'B', 'D', 'E', 'G', 'H', 'J', 'K'],
#        ['A', 'B', 'D', 'E', 'G', 'H', 'J', 'K'],
#        ['A', 'B', 'D', 'E', 'G', 'H', 'J', 'K'],
#        ['A', 'B', 'D', 'E', 'G', 'H', 'J', 'K'],
#        ['A', 'B', 'D', 'E', 'G', 'H', 'J', 'K']], dtype='<U1')

# Example for juxtapose
arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(spb.juxtapose(arr3, 3, 1))
# Output:
# array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
#        [1, 2, 3, 1, 2, 3, 1, 2, 3],
#        [1, 2, 3, 1, 2, 3, 1, 2, 3]])

# Example for mosaic
print(spb.mosaic(arr3, (2, 2)))
# Output:
# array([[1, 2, 3, 1, 2, 3],
#        [1, 2, 3, 1, 2, 3],
#        [1, 2, 3, 1, 2, 3],
#        [1, 2, 3, 1, 2, 3]])
