import numpy as np
import matplotlib.pyplot as plt

def plot_with_loss(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, one-dimensional array of size m.
    y: has to be an numpy.ndarray, one-dimensional array of size m.
    theta: has to be an numpy.ndarray, one-dimensional array of size 2.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.ndim != 1 or y.ndim != 1 or x.size != y.size or theta.ndim != 1 or theta.size != 2:
        return None
    if x.size == 0 or y.size == 0:
        return None

    yhat = theta[0] + theta[1] * x
    J = np.mean((yhat - y) ** 2)

    # when no argument is passed, subplots() returns a figure (window where the graph is drawn) 
    # and a single graph (containing vertical and horizontal axes)
    fig, ax = plt.subplots()
    # scatter() displays individual data points on a graph
    # where the coordinates correspond to each value in the array x and y 
    ax.scatter(x, y, color='blue')
    # plot() displays a line plot on a graph
    # by connecting each data points with coord x and yhat
    ax.plot(x, yhat, color='orange')
    # Plot vertical lines showing errors (distance between points and prediction line)
    for i in range(len(x)):
        ax.plot([x[i], x[i]], [y[i], yhat[i]], linestyle='--', color='red', linewidth=1)
    ax.set_title(f'Cost: {J:.2f}')
    plt.show()

x = np.arange(1,6)
y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])

theta1= np.array([18,-1])
plot_with_loss(x, y, theta1)

theta2 = np.array([14, 0])
plot_with_loss(x, y, theta2)

theta3 = np.array([12, 0.8])
plot_with_loss(x, y, theta3)
