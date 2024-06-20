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
    if x.shape[0] == 0 or x.shape[1] != 1:
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
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    m = x.shape[0]
    n = x.shape[1]
    if m == 0 or n + 1 != theta.shape[0] or theta.shape[1] != 1:
        return None
    X_prime = np.c_[np.ones(m), x]
    e = np.exp(-X_prime @ theta)
    return 1 / (1 + e)


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
    

y1 = np.array([1]).reshape((-1, 1))
x1 = np.array([4]).reshape((-1, 1))
theta1 = np.array([[2], [0.5]])
print(log_gradient(x1, y1, theta1))
# Output:
# array([[-0.01798621],
# [-0.07194484]])

y2 = np.array([[1], [0], [1], [0], [1]])
x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
theta2 = np.array([[2], [0.5]])
print(log_gradient(x2, y2, theta2))
# Output:
# array([[0.3715235 ],
# [3.25647547]])

y3 = np.array([[0], [1], [1]])
x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
print(log_gradient(x3, y3, theta3))
# Output:
# array([[-0.55711039],
# [-0.90334809],
# [-2.01756886],
# [-2.10071291],
# [-3.27257351]])
