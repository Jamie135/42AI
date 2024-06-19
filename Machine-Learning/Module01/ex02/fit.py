import numpy as np

def simple_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array, with a for-loop.
    The three arrays must have compatible shapes.
    Args:
    x: has to be an numpy.array, a vector of shape m * 1.
    y: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be an numpy.array, a 2 * 1 vector.
    Return:
    The gradient as a numpy.array, a vector of shape 2 * 1.
    None if x, y, or theta are empty numpy.array.
    None if x, y and theta do not have compatible shapes.
    None if x, y or theta is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return None
    if x.shape[0] != y.shape[0] or theta.shape != (2, 1):
        return None
    
    m = x.shape[0]
    # add a column of ones to x to create a matrix X0
    X0 = np.hstack((np.ones((m, 1)), x))
    # with X0 as a matrix, we can now use vectorization instead of for loop
    # to calculate the error array and use error to calculate the gradient array
    error = np.dot(X0, theta) - y
    # .T is a method to transpose a matrix
    gradient = np.dot(X0.T, error) / m
    return gradient


def fit_(x, y, theta, alpha, max_iter):
    """
    Description:
    Fits the model to the training dataset contained in x and y.
    Args:
    x: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
    y: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
    theta: has to be a numpy.ndarray, a vector of dimension 2 * 1.
    alpha: has to be a float, the learning rate
    max_iter: has to be an int, the number of iterations done during the gradient descent
    Returns:
    new_theta: numpy.ndarray, a vector of dimension 2 * 1.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exception.
    """
    if x.ndim != 2 or y.ndim != 2 or theta.ndim != 2 or x.shape[1] != 1 or y.shape[1] != 1 or theta.shape != (2, 1):
        return None
    for _ in range(max_iter):
        gradient = simple_gradient(x, y, theta)
        theta = theta - alpha * gradient
    return theta


x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
theta = np.array([1, 1]).reshape((-1, 1))

theta1 = fit_(x, y, theta, alpha=5e-8, max_iter=1500000)
print(theta1)

def predict(x, theta):
    """
    Computes the vector of prediction y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a one-dimensional array of size m.
    theta: has to be an numpy.array, a two-dimensional array of shape 2 * 1.
    Returns:
    y_hat as a numpy.array, a two-dimensional array of shape m * 1.
    None if x and/or theta are not numpy.array.
    None if x or theta are empty numpy.array.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exceptions.
    """
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.ndim != 2 or theta.ndim != 2 or theta.shape != (2, 1):
        return None
    
    X0 = np.c_[np.ones((x.shape[0], 1)), x]
    y_hat = np.dot(X0, theta)
    return y_hat

print(predict(x, theta1))
