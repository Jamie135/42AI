import numpy as np

def add_polynomial_features(x, power):
    """Add polynomial features to vector x by raising its values up to the power given in argument.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    power: has to be an int, the power up to which the components of vector x are going to be raised.
    Return:
    The matrix of polynomial features as a numpy.array, of dimension m * n,
    containing the polynomial feature values for all training examples.
    None if x is an empty numpy.array.
    None if x or power is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(power, int):
            return None
    elif x.shape[0] == 0 or x.shape[1] == 0 or power < 1:
        return None
    
    # initialize the list to store polynomial features
    poly_features = []
    
    # iterate over each power from 1 to the given power
    for p in range(1, power + 1):
        poly_features.append(x ** p)
    
    # Concatenate all the polynomial features along the second axis (columns)
    poly_matrix = np.concatenate(poly_features, axis=1)
    
    return poly_matrix
    

x = np.arange(1,11).reshape(5, 2)
# Example 1:
print(add_polynomial_features(x, 3))
# Output:
# array([[ 1, 2, 1, 4, 1, 8],
# [ 3, 4, 9, 16, 27, 64],
# [ 5, 6, 25, 36, 125, 216],
# [ 7, 8, 49, 64, 343, 512],
# [ 9, 10, 81, 100, 729, 1000]])

# Example 2:
print(add_polynomial_features(x, 4))
# Output:
# array([[ 1, 2, 1, 4, 1, 8, 1, 16],
# [ 3, 4, 9, 16, 27, 64, 81, 256],
# [ 5, 6, 25, 36, 125, 216, 625, 1296],
# [ 7, 8, 49, 64, 343, 512, 2401, 4096],
# [ 9, 10, 81, 100, 729, 1000, 6561, 10000]])
