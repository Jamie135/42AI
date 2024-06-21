import numpy as np
import sklearn.metrics as skm

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


def vec_log_loss_(y, y_hat, eps=1e-15):
    """
    Computes the logistic loss value.
    Args:
    y: has to be an numpy.ndarray, a vector of shape m * 1.
    y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
    eps: has to be a float, epsilon (default=1e-15)
    Returns:
    The logistic loss value as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray) or not isinstance(eps, (int, float)):
        return None
    m = y.shape[0]
    if y.shape != y_hat.shape or m == 0:
        return None
    
    # avoid log(0) that = nan (-infinity)
    y_hat_eps = np.clip(y_hat, eps, 1 - eps)
    loss = (np.dot(y.T, np.log(y_hat_eps)) + np.dot((1 - y).T, np.log(1 - y_hat_eps)))[0, 0]
    return (-1 / m) * loss 


def reg_log_loss_(y, y_hat, theta, lambda_):
    """Computes the regularized loss of a logistic regression model from two non-empty numpy.ndarray, without any for lArgs:
    y: has to be an numpy.ndarray, a vector of shape m * 1.
    y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    lambda_: has to be a float.
    Returns:
    The regularized loss as a float.
    None if y, y_hat, or theta is empty numpy.ndarray.
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
    
    J_logistic = vec_log_loss_(y, y_hat)
    l2_reg = l2(theta)
    J = J_logistic + (lambda_ / (2 * m)) * l2_reg
    return float(J)
    

if __name__ == "__main__":

    y = np.array([1, 1, 0, 0, 1, 1, 0]).reshape((-1, 1))
    y_hat = np.array([.9, .79, .12, .04, .89, .93, .01]).reshape((-1, 1))
    theta = np.array([1, 2.5, 1.5, -0.9]).reshape((-1, 1))

    # Example :
    print(reg_log_loss_(y, y_hat, theta, .5))
    # Output:
    # 0.43377043716475955

    # Example :
    print(reg_log_loss_(y, y_hat, theta, .05))
    # Output:
    # 0.13452043716475953

    # Example :
    print(reg_log_loss_(y, y_hat, theta, .9))
    # Output:
    # 0.6997704371647596
