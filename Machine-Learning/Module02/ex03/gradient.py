import numpy as np

def gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array, without any for-loop.
    The three arrays must have the compatible dimensions.
    Args:
    x: has to be an numpy.array, a matrix of dimension m * n.
    y: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector (n +1) * 1.
    Return:
    The gradient as a numpy.array, a vector of dimensions n * 1,
    containing the result of the formula for all j.
    None if x, y, or theta are empty numpy.array.
    None if x, y and theta do not have compatible dimensions.
    None if x, y or theta is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    for array in [x, y]:
        if not isinstance(array, np.ndarray):
            return None
    m, n = x.shape
    if m == 0 or n == 0:
        return None
    elif y.shape != (m, 1):
        return None
    elif theta.shape != (n + 1, 1):
        return None
    # add a column of ones to x to create a matrix X0
    X_prime = np.c_[np.ones(m), x]
    # with Xprime as a matrix, we can now use vectorization instead of for loop
    # to calculate the error array (theta - y)
    # we can use @ instead of dot()
    # .T is a method to transpose a matrix
    return (X_prime.T @ (X_prime @ theta - y)) / m


if __name__ == "__main__":
    x = np.array([
        [ -6, -7, -9],
        [ 13, -2, 14],
        [ -7, 14, -1],
        [ -8, -4, 6],
        [ -5, -9, 6],
        [ 1, -5, 11],
        [ 9, -11, 8]
    ])
    y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
    theta1 = np.array([0, 3, 0.5, -6]).reshape((-1, 1))
    
    print(gradient(x, y, theta1))  # Expected output: [[ -33.71428571], [ -37.35714286], [183.14285714], [-393.]]
    
    theta2 = np.array([0, 0, 0, 0]).reshape((-1, 1))
    print(gradient(x, y, theta2))  # Expected output: [[ -0.71428571], [ 0.85714286], [23.28571429], [-26.42857143]]
