import numpy as np

def simple_predict(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a one-dimensional array of size m.
    theta: has to be an numpy.ndarray, a one-dimensional array of size 2.
    Returns:
    y_hat as a numpy.ndarray, a one-dimensional array of size m.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray) or x.ndim != 1 or theta.ndim != 1:
        return None
    if x.size == 0 or theta.size !=2:
        return None
    
    return theta[0] + theta[1] * x


x = np.arange(1, 6)
print(f"x = {x}")
theta1 = np.array([5, 0])
print(simple_predict(x, theta1))  # Output: array([5., 5., 5., 5., 5.])

theta2 = np.array([0, 1])
print(simple_predict(x, theta2))  # Output: array([1., 2., 3., 4., 5.])

theta3 = np.array([5, 3])
print(simple_predict(x, theta3))  # Output: array([ 8., 11., 14., 17., 20.])

theta4 = np.array([-3, 1])
print(simple_predict(x, theta4))  # Output: array([-2., -1., 0., 1., 2.])
      