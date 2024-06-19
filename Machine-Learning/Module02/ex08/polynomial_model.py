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
    if x.size == 0 or x.shape[1] != 1:
        return None
    
    return np.hstack([x ** i for i in range(1, power + 1)])
    # m = x.shape[0]
    # vandermonde = np.zeros((m, power))
    # for i in range (1, power + 1):
    #     # assign all value of each row from x, power by i, 
    #     # to the i-1 column of all rows in vandermonde
    #     vandermonde[:, i - 1] = x[:, 0] ** i
    # return vandermonde
