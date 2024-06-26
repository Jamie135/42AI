import numpy as np

def simple_predict(x, theta):
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
    
    return np.dot(x, theta[1:]) + theta[0]


# Examples
x = np.arange(1, 13).reshape((4, -1))

# Example 1:
theta1 = np.array([5, 0, 0, 0]).reshape((-1, 1))
print(simple_predict(x, theta1))
# Output: array([[5.], [5.], [5.], [5.]])

# Example 2:
theta2 = np.array([0, 1, 0, 0]).reshape((-1, 1))
print(simple_predict(x, theta2))
# Output: array([[ 1.], [ 4.], [ 7.], [10.]])

# Example 3:
theta3 = np.array([-1.5, 0.6, 2.3, 1.98]).reshape((-1, 1))
print(simple_predict(x, theta3))
# Output: array([[ 9.64], [24.28], [38.92], [53.56]])

# Example 4:
theta4 = np.array([-3, 1, 2, 3.5]).reshape((-1, 1))
print(simple_predict(x, theta4))
# Output: array([[12.5], [32. ], [51.5], [71. ]])
