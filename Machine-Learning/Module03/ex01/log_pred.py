import numpy as np

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


# Example usage:
x = np.array([4]).reshape((-1, 1))
theta = np.array([[2], [0.5]])
print(logistic_predict_(x, theta))
# Output: array([[0.98201379]])

x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
theta2 = np.array([[2], [0.5]])
print(logistic_predict_(x2, theta2))
# Output: array([[0.98201379], [0.99624161], [0.97340301], [0.99875204], [0.90720705]])

x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
print(logistic_predict_(x3, theta3))
# Output: array([[0.03916572], [0.00045262], [0.2890505 ]])

