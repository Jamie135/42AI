import numpy as np

def sigmoid_(x):
    """
    Compute the sigmoid of a vector.
    Args:
    x: has to be a numpy.ndarray of shape (m, 1).
    Returns:
    The sigmoid value as a numpy.ndarray of shape (m, 1).
    None if x is an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray):
        return None
    e = np.exp(-x)
    return 1 / (1 + e)


def logistic_predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * n.
    theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exception.
    """
    if not all([isinstance(arr, np.ndarray) for arr in [x, theta]]):
        return None

    m, n = x.shape

    if m == 0 or n == 0:
        return None
    elif theta.shape != (n + 1, 1):
        return None
    X_prime = np.c_[np.ones(m), x]
    return sigmoid_(X_prime @ theta)


def log_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.ndarray, with a for-loop. The three arrays must have compatiblArgs:
    x: has to be an numpy.ndarray, a matrix of shape m * n.
    y: has to be an numpy.ndarray, a vector of shape m * 1.
    theta: has to be an numpy.ndarray, a vector of shape (n + 1) * 1.
    Returns:
    The gradient as a numpy.ndarray, a vector of shape n * 1, containing the result of the formula for all j.
    None if x, y, or theta are empty numpy.ndarray.
    None if x, y and theta do not have compatible dimensions.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    m, n = x.shape
    if m == 0 or m != y.shape[0] or n + 1 != theta.shape[0] or y.shape[1] != theta.shape[1] or theta.shape[1] != 1:
        return None
    
    y_hat = logistic_predict_(x, theta)
    if y_hat is None:
        return None
    
    gradient = np.zeros((n + 1, 1))
    gradient[0] = np.sum(y_hat - y)
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            gradient[j] += (y_hat[i - 1] - y[i - 1]) * x[i - 1, j - 1]
    return gradient / m    


def checkargs(func):

    def wrapper(y, x, theta, lambda_):
        try:
            if not isinstance(y, np.ndarray) \
                or not isinstance(x, np.ndarray) \
                    or not isinstance(theta, np.ndarray):
                return None
            m, n = x.shape
            if m == 0 or n == 0:
                return None
            if y.shape != (m, 1) \
                or x.shape != (m, n) \
                    or theta.shape != (n + 1, 1):
                return None
            if not isinstance(lambda_, (int, float)):
                return None
            return func(y, x, theta, lambda_)
        except Exception:
            return None

    return wrapper


@checkargs
def reg_logistic_grad(y, x, theta, lambda_):
    """Computes the regularized logistic gradient of three non-empty numpy.ndarray, with two for-loops. The three arrayArgs:
    y: has to be a numpy.ndarray, a vector of shape m * 1.
    x: has to be a numpy.ndarray, a matrix of dimesion m * n.
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    lambda_: has to be a float.
    Returns:
    A numpy.ndarray, a vector of shape n * 1, containing the results of the formula for all j.
    None if y, x, or theta are empty numpy.ndarray.
    None if y, x or theta does not share compatibles shapes.
    Raises:
    This function should not raise any Exception.
    """
    m, n = x.shape
    y_hat = logistic_predict_(x, theta)
    if y_hat is None:
        return None
    gradient = np.zeros((n + 1, 1))
    gradient[0, 0] = np.sum(y_hat - y)
    for j in range(1, n + 1):
        for i in range(m):
            gradient[j] += (y_hat[i] - y[i]) * x[i, j - 1]
        gradient[j, 0] += lambda_ * theta[j, 0]
    return gradient / m


@checkargs
def vec_reg_logistic_grad(y, x, theta, lambda_):
    """Computes the regularized logistic gradient of three non-empty numpy.ndarray, without any for-loop. The three arrArgs:
    y: has to be a numpy.ndarray, a vector of shape m * 1.
    x: has to be a numpy.ndarray, a matrix of shape m * n.
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    lambda_: has to be a float.
    Returns:
    A numpy.ndarray, a vector of shape n * 1, containing the results of the formula for all j.
    None if y, x, or theta are empty numpy.ndarray.
    None if y, x or theta does not share compatibles shapes.
    Raises:
    This function should not raise any Exception.
    """
    m = x.shape[0]
    X1 = np.hstack((np.ones((m, 1)), x))
    y_hat = logistic_predict_(x, theta)
    if y_hat is None:
        return None
    theta0 = theta.copy()
    theta0[0, 0] = 0.0
    return (X1.T.dot(y_hat - y) + (lambda_ * theta0)) / m


if __name__ == "__main__":

    x = np.array([[0, 2, 3, 4],
                  [2, 4, 5, 5],
                  [1, 3, 2, 7]])

    y = np.array([[0], [1], [1]])

    theta = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])

    # Example 1.1:
    print(reg_logistic_grad(y, x, theta, 1))
    # Output:
    # array([[-0.55711039],
    #     [-1.40334809],
    #     [-1.91756886],
    #     [-2.56737958],
    #     [-3.03924017]])

    # Example 1.2:
    print(vec_reg_logistic_grad(y, x, theta, 1))
    # Output:
    # array([[-0.55711039],
    #     [-1.40334809],
    #     [-1.91756886],
    #     [-2.56737958],
    #     [-3.03924017]])

    # Example 2.1:
    print(reg_logistic_grad(y, x, theta, 0.5))
    # Output:
    # array([[-0.55711039],
    #     [-1.15334809],
    #     [-1.96756886],
    #     [-2.33404624],
    #     [-3.15590684]])

    # Example 2.2:
    print(vec_reg_logistic_grad(y, x, theta, 0.5))
    # Output:
    # array([[-0.55711039],
    #     [-1.15334809],
    #     [-1.96756886],
    #     [-2.33404624],
    #     [-3.15590684]])

    # Example 3.1:
    print(reg_logistic_grad(y, x, theta, 0.0))
    # Output:
    # array([[-0.55711039],
    #     [-0.90334809],
    #     [-2.01756886],
    #     [-2.10071291],
    #     [-3.27257351]])

    # Example 3.2:
    print(vec_reg_logistic_grad(y, x, theta, 0.0))
    # Output:
    # array([[-0.55711039],
    #     [-0.90334809],
    #     [-2.01756886],
    #     [-2.10071291],
    #     [-3.27257351]])
