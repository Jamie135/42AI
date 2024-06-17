import numpy as np

def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.array.
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
    if x.ndim != 1 or theta.shape != (2, 1):
        return None
    if x.size == 0 or theta.size == 0:
        return None
    
    # np.c_ concatenates arrays along the second axis (column-wise)
    # so here X0 will concatenate the column of ones with the column x
    X0 = np.c_[np.ones(x.shape[0]), x]
    
    # compute the predicted values y_hat using dot to multiply X0 matrix with theta vector
    yhat = X0.dot(theta)
    
    return yhat


if __name__ == "__main__":
    x = np.arange(1, 6)

    # Example 1:
    theta1 = np.array([[5], [0]])
    print(predict_(x, theta1))
    # Output: array([[5.], [5.], [5.], [5.], [5.]])

    # Example 2:
    theta2 = np.array([[0], [1]])
    print(predict_(x, theta2))
    # Output: array([[1.], [2.], [3.], [4.], [5.]])
    
    # Example 3:
    theta3 = np.array([[5], [3]])
    print(predict_(x, theta3))
    # Output: array([[ 8.], [11.], [14.], [17.], [20.]])
    
    # Example 4:
    theta4 = np.array([[-3], [1]])
    print(predict_(x, theta4))
    # Output: array([[-2.], [-1.], [ 0.], [ 1.], [ 2.]])
