import numpy as np

def checkargs(func):

    def wrapper(y, x, theta, lambda_):
        try:
            if not (isinstance(y, np.ndarray) and isinstance(x, np.ndarray) and isinstance(theta, np.ndarray) and isinstance(lambda_, (float, int))):
                return None
            if y.size == 0 or x.size == 0 or theta.size == 0:
                return None
            if y.shape[0] != x.shape[0] or x.shape[1] + 1 != theta.shape[0] or y.shape[1] != 1 or theta.shape[1] != 1:
                return None
            return func(y, x, theta, lambda_)
        except Exception:
            return None

    return wrapper


@checkargs
def reg_linear_grad(y, x, theta, lambda_):
    """Computes the regularized linear gradient of three non-empty numpy.ndarray, with two for-loop.
    Args:
    y: has to be a numpy.ndarray, a vector of shape m * 1.
    x: has to be a numpy.ndarray, a matrix of dimension m * n.
    theta: has to be a numpy.ndarray, a vector of shape (n + 1) * 1.
    lambda_: has to be a float.
    Return:
    A numpy.ndarray, a vector of shape (n + 1) * 1, containing the results of the formula for all j.
    None if y, x, or theta are empty numpy.ndarray.
    None if y, x or theta does not share compatible shapes.
    None if y, x or theta or lambda_ is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    m, n = x.shape
    grad = np.zeros((n + 1, 1))
    y_hat = x.dot(theta[1:]) + theta[0]
    error = y_hat - y
    
    grad[0] = np.sum(error) / m
    for j in range(1, n + 1):
        grad[j] = (np.sum(error * x[:, j - 1].reshape(-1, 1)) + lambda_ * theta[j]) / m
    
    return grad


@checkargs
def vec_reg_linear_grad(y, x, theta, lambda_):
    """Computes the regularized linear gradient of three non-empty numpy.ndarray, without any for-loop.
    Args:
    y: has to be a numpy.ndarray, a vector of shape m * 1.
    x: has to be a numpy.ndarray, a matrix of dimension m * n.
    theta: has to be a numpy.ndarray, a vector of shape (n + 1) * 1.
    lambda_: has to be a float.
    Return:
    A numpy.ndarray, a vector of shape (n + 1) * 1, containing the results of the formula for all j.
    None if y, x, or theta are empty numpy.ndarray.
    None if y, x or theta does not share compatible shapes.
    None if y, x or theta or lambda_ is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    m = y.shape[0]
    x0 = np.c_[np.ones((m, 1)), x]
    y_hat = x0.dot(theta)
    error = y_hat - y
    
    theta_reg = np.copy(theta)
    theta_reg[0] = 0
    
    grad = (x0.T.dot(error) + lambda_ * theta_reg) / m
    
    return grad


if __name__ == "__main__":

    x = np.array([[-6, -7, -9],
                  [13, -2, 14],
                  [-7, 14, -1],
                  [-8, -4, 6],
                  [-5, -9, 6],
                  [1, -5, 11],
                  [9, -11, 8]])
    y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
    theta = np.array([[7.01], [3], [10.5], [-6]])

    # Example 1.1:
    print(reg_linear_grad(y, x, theta, 1))
    print()
    # Output:
    # array([[ -60.99 ],
    #        [-195.64714286],
    #        [ 863.46571429],
    #        [-644.52142857]])

    # Example 1.2:
    print(vec_reg_linear_grad(y, x, theta, 1))
    print()
    # Output:
    # array([[ -60.99 ],
    #        [-195.64714286],
    #        [ 863.46571429],
    #        [-644.52142857]])

    # Example 2.1:
    print(reg_linear_grad(y, x, theta, 0.5))
    print()
    # Output:
    # array([[ -60.99 ],
    #        [-195.86142857],
    #        [ 862.71571429],
    #        [-644.09285714]])

    # Example 2.2:
    print(vec_reg_linear_grad(y, x, theta, 0.5))
    print()
    # Output:
    # array([[ -60.99 ],
    #        [-195.86142857],
    #        [ 862.71571429],
    #        [-644.09285714]])

    # Example 3.1:
    print(reg_linear_grad(y, x, theta, 0.0))
    print()
    # Output:
    # array([[ -60.99 ],
    #        [-196.07571429],
    #        [ 861.96571429],
    #        [-643.66428571]])

    # Example 3.2:
    print(vec_reg_linear_grad(y, x, theta, 0.0))
    print()
    # Output:
    # array([[ -60.99 ],
    #        [-196.07571429],
    #        [ 861.96571429],
    #        [-643.66428571]])
