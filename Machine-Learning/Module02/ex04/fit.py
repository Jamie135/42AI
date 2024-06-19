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
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return None
    m, n = x.shape
    if y.shape != (m, 1) or theta.shape != (n + 1, 1):
        return None
    
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
    x: has to be a numpy.array, a matrix of dimension m * n:
    (number of training examples, number of features).
    y: has to be a numpy.array, a vector of dimension m * 1:
    (number of training examples, 1).
    theta: has to be a numpy.array, a vector of dimension (n + 1) * 1:
    (number of features + 1, 1).
    alpha: has to be a float, the learning rate
    max_iter: has to be an int, the number of iterations done during the gradient descent
    Return:
    new_theta: numpy.array, a vector of dimension (number of features + 1, 1).
    None if there is a matching dimension problem.
    None if x, y, theta, alpha or max_iter is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    m, n = x.shape
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return None
    if y.shape != (m, 1) or theta.shape != (n + 1, 1):
        return None
    for _ in range(max_iter):
        grad = gradient(x, y, theta)
        theta = theta - alpha * grad
    return theta


x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta = np.array([[42.], [1.], [1.], [1.]])
# Example 0:
theta2 = fit_(x, y, theta, alpha = 0.0005, max_iter=42000)
print(theta2)
# Output: array([[41.99..],[0.97..], [0.77..], [-1.20..]])
# Example 1:

def predict_(x, theta):
    """
    Computes the prediction vector y_hat from two non-empty numpy.array.
    
    Args:
    x: has to be an numpy.array, a matrix of dimension m * n.
    theta: has to be an numpy.array, a vector of dimension (n + 1) * 1.
    
    Return:
    y_hat as a numpy.array, a vector of dimension m * 1.
    None if x or theta are empty numpy.array.
    None if x or theta dimensions are not matching.
    None if x or theta is not of expected type.
    
    Raises:
    This function should not raise any Exception.
    """
    
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or theta.size == 0:
        return None
    if theta.shape[0] != x.shape[1] + 1:
        return None
    
    # Add a column of ones to x to account for theta0
    X0 = np.hstack((np.ones((x.shape[0], 1)), x))
    
    # Compute the prediction
    y_hat = X0.dot(theta)
    
    return y_hat

print(predict_(x, theta2))
# Output: array([[19.5992..], [-2.8003..], [-25.1999..], [-47.5996..]])
