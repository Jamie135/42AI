import numpy as np

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


def reg_loss_(y, y_hat, theta, lambda_):
    """Computes the regularized loss of a linear regression model from two non-empty numpy.array, without any for loop.Args:
    y: has to be an numpy.ndarray, a vector of shape m * 1.
    y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    lambda_: has to be a float.
    Returns:
    The regularized loss as a float.
    None if y, y_hat, or theta are empty numpy.ndarray.
    None if y and y_hat do not share the same shapes.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(y, np.ndarray) \
        or not isinstance(y_hat, np.ndarray) \
        or not isinstance(theta, np.ndarray) \
        or not isinstance(lambda_, float):
        return None
    m = y.shape[0]
    n = theta.shape[0]
    if m == 0 or n == 0:
        return None
    if y.shape != (m, 1) \
        or y_hat.shape != (m, 1) \
        or theta.shape != (n, 1):
        return None
    J_elem = (y_hat - y).T @ (y_hat - y)
    l2_reg = l2(theta)
    J = (1 / (2 * m)) * np.sum(J_elem + (lambda_ * l2_reg))
    return float(J)


    

if __name__ == "__main__":

    y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
    y_hat = np.array([3, 13, -11.5, 5, 11, 5, -20]).reshape((-1, 1))
    theta = np.array([1, 2.5, 1.5, -0.9]).reshape((-1, 1))

    # Example :
    print(reg_loss_(y, y_hat, theta, .5))
    # Output:
    # 0.8503571428571429

    # Example :
    print(reg_loss_(y, y_hat, theta, .05))
    # Output:
    # 0.5511071428571429

    # Example :
    print(reg_loss_(y, y_hat, theta, .9))
    # Output:
    # 1.1163571428571428
