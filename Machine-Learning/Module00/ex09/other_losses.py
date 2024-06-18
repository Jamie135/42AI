import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt

def mse_(y, y_hat):
    """
    Description:
    Calculate the MSE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a two-dimensional array of shape m * 1.
    y_hat: has to be a numpy.array, a two-dimensional vector of shape m * 1.
    Returns:
    mse: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    if y.shape != y_hat.shape:
        return None
    if y.ndim != 2 or y.shape[1] != 1:
        return None
    
    SE = (y_hat - y) ** 2
    return np.mean(SE)


def rmse_(y, y_hat):
    """
    Description:
    Calculate the RMSE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a two-dimensional array of shape m * 1.
    y_hat: has to be a numpy.array, a two-dimensional array of shape m * 1.
    Returns:
    rmse: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    MSE = mse_(y, y_hat)
    if MSE is None:
        return None
    return MSE ** 0.5


def mae_(y, y_hat):
    """
    Description:
    Calculate the MAE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a two-dimensional array of shape m * 1.
    y_hat: has to be a numpy.array, a two-dimensional array of shape m * 1.
    Returns:
    mae: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    if y.shape != y_hat.shape:
        return None
    if y.ndim != 2 or y.shape[1] != 1:
        return None
    
    AE = abs(y_hat - y)
    return np.mean(AE)


def r2score_(y, y_hat):
    """
    Description:
    Calculate the R2score between the predicted output and the output.
    Args:
    y: has to be a numpy.array, a two-dimensional array of shape m * 1.
    y_hat: has to be a numpy.array, a two-dimensional array of shape m * 1.
    Returns:
    r2score: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
        return None
    if y.shape != y_hat.shape:
        return None
    if y.ndim != 2 or y.shape[1] != 1:
        return None
    
    ymean = np.mean(y)

    # calculate total sum of squares
    SS = np.sum((y - ymean)**2)
    
    # calculate residual sum of squares
    RS = np.sum((y - y_hat)**2)
    
    # calculate and return the R-squared score
    return 1 - (RS / SS)


x = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])

# Mean squared error
## your implementation
print(mse_(x,y))
## Output: 4.285714285714286
## sklearn implementation
print(mean_squared_error(x,y))
## Output: 4.285714285714286

# Root mean squared error
## your implementation
print(rmse_(x,y))
## Output: 2.0701966780270626
## sklearn implementation not available: take the square root of MSE
print(sqrt(mean_squared_error(x,y)))
## Output: 2.0701966780270626

# Mean absolute error
## your implementation
print(mae_(x,y))
# Output: 1.7142857142857142
## sklearn implementation
print(mean_absolute_error(x,y))
# Output: 1.7142857142857142

# R2-score
## your implementation
print(r2score_(x,y))
## Output: 0.9681721733858745
## sklearn implementation
print(r2_score(x,y))
## Output: 0.968172173385874
