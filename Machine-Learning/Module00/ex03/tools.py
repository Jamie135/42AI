import numpy as np

def add_intercept(x):
    """Adds a column of 1’s to the non-empty numpy.array x.
    Args:
    x: has to be a numpy.array. x can be a one-dimensional (m * 1) or two-dimensional (m * n) array.
    Returns:
    X, a numpy.array of dimension m * (n + 1).
    None if x is not a numpy.array.
    None if x is an empty numpy.array.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or x.size == 0:
        return None
    if x.ndim == 1:
        # reshape turns a 1D x into a 2D x
        # -1 is a placeholder to tell NumPy to calculate the appropriate dimension 
        # based on the length of the array and the specified dimension 1
        x = x.reshape(-1, 1)
    # creates a column vector of ones with the same number of rows as x
    vect_one = np.ones((x.shape[0], 1))
    # horizontally stacks the intercept column with the original array
    return np.hstack((vect_one, x))


if __name__ == "__main__":
    # Example 1:
    x = np.arange(1, 6)
    print(add_intercept(x))
    # Output:
    # array([[1., 1.],
    #        [1., 2.],
    #        [1., 3.],
    #        [1., 4.],
    #        [1., 5.]])

    # Example 2:
    y = np.arange(1, 10).reshape((3, 3))
    print(add_intercept(y))
    # Output:
    # array([[1., 1., 2., 3.],
    #        [1., 4., 5., 6.],
    #        [1., 7., 8., 9.]])
