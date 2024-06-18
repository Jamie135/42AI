import numpy as np
import matplotlib.pyplot as plt

def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a one-dimensional array of size m.
    y: has to be an numpy.array, a one-dimensional array of size m.
    theta: has to be an numpy.array, a two-dimensional array of shape 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exceptions.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.ndim != 1 or y.ndim != 1 or theta.shape != (2, 1):
        return None
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return None
    
    yhat = theta[0, 0] + theta[1, 0] * x

    # when no argument is passed, subplots() returns a figure (window where the graph is drawn) 
    # and a single graph (containing vertical and horizontal axes)
    fig, ax = plt.subplots()
    # scatter() displays individual data points on a graph
    # where the coordinates correspond to each value in the array x and y 
    ax.scatter(x, y, color='blue')
    # plot() displays a line plot on a graph
    # by connecting each data points with coord x and yhat
    ax.plot(x, yhat, color='orange')
    plt.show()


x = np.arange(1,6)
y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])

# Example 1:
theta1 = np.array([[4.5],[-0.2]])
plot(x, y, theta1)

# Example 2:
theta2 = np.array([[-1.5],[2]])
plot(x, y, theta2)

# Example 3:
theta3 = np.array([[3],[0.3]])
plot(x, y, theta3)
