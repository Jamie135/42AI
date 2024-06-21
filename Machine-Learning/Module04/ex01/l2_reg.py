import numpy as np

def iterative_l2(theta):
    """Computes the L2 regularization of a non-empty numpy.ndarray, with a for-loop.
    Args:
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    Returns:
    The L2 regularization as a float.
    None if theta in an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(theta, np.ndarray) or theta.shape[0] == 0 or theta.shape[1] != 1:
        return None
    l2 = 0
    for j in range(1, theta.shape[0]):
        l2 += theta[j, 0] ** 2
    return float(l2)


def l2(theta):
    """Computes the L2 regularization of a non-empty numpy.ndarray, without any for-loop.
    Args:
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    Returns:
    The L2 regularization as a float.
    None if theta in an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(theta, np.ndarray) or theta.shape[0] == 0 or theta.shape[1] != 1:
        return None
    tmp = np.copy(theta)
    tmp[0] = 0
    l2 = np.dot(tmp.T, tmp)
    return float(l2[0, 0])
    

# Examples to test the functions
x = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
print(iterative_l2(x))  # Output: 911.0
print(l2(x))            # Output: 911.0

y = np.array([3, 0.5, -6]).reshape((-1, 1))
print(iterative_l2(y))  # Output: 36.25
print(l2(y))            # Output: 36.25
