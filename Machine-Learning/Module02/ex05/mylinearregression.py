import numpy as np

class MyLinearRegression():
    """
    Description:
    My personnal linear regression class to fit like a boss.
    """

    def __init__(self, thetas, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = np.array(thetas)

    @staticmethod
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


    def fit_(self, x, y):
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
        if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(self.thetas, np.ndarray):
            return None
        if x.size == 0 or y.size == 0 or self.thetas.size == 0:
            return None
        if y.shape != (m, 1) or self.thetas.shape != (n + 1, 1):
            return None
        for _ in range(self.max_iter):
            grad = self.gradient(x, y, self.thetas)
            self.thetas = self.thetas - self.alpha * grad
        return self.thetas
    
    
    def predict_(self, x):
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
        if not isinstance(x, np.ndarray) or not isinstance(self.thetas, np.ndarray):
            return None
        if x.size == 0 or self.thetas.size == 0:
            return None
        if self.thetas.shape[0] != x.shape[1] + 1:
            return None
        
        # Add a column of ones to x to account for theta0
        X0 = np.hstack((np.ones((x.shape[0], 1)), x))
        
        # Compute the prediction
        y_hat = X0.dot(self.thetas)
        
        return y_hat
    

    def loss_elem_(self, y, y_hat):
        """
        Description:
        Calculates all the elements (y_pred - y)^2 of the loss function.
        Args:
        y: has to be a numpy.array, a two-dimensional array of shape m * 1.
        y_hat: has to be a numpy.array, a two-dimensional array of shape m * 1.
        Returns:
        J_elem: numpy.array, an array of dimension (number of the training examples, 1).
        None if there is a dimension matching problem.
        None if any argument is not of the expected type.
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
            return None
        if y.shape != y_hat.shape or y.size == 0 or y_hat.size == 0:
            return None
        if y.ndim != y_hat.ndim or y.size != y_hat.size:
            return None

        J_elem = (y_hat - y) ** 2
        return J_elem
    

    def loss_(self, y, y_hat):
        """Computes the half mean squared error of two non-empty numpy.array, without any for loop.
        The two arrays must have the same dimensions.
        Args:
        y: has to be an numpy.array, a one-dimensional array of size m.
        y_hat: has to be an numpy.array, a one-dimensional array of size m.
        Returns:
        The half mean squared error of the two vectors as a float.
        None if y or y_hat are empty numpy.array.
        None if y and y_hat does not share the same dimensions.
        Raises:
        This function should not raise any Exceptions.
        """
        J = self.loss_elem_(y, y_hat)
        if J is None:
            return None
        return np.mean(J) / 2
    

X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
Y = np.array([[23.], [48.], [218.]])

mylr = MyLinearRegression([[1.], [1.], [1.], [1.], [1]])
# Example 0:
y_hat = mylr.predict_(X)
print(y_hat)
# Output: array([[8.], [48.], [323.]])
# Example 1:
print(mylr.loss_elem_(Y, y_hat))
# Output: array([[225.], [0.], [11025.]])
# Example 2:
print(mylr.loss_(Y, y_hat))
# Output: 1875.0
# Example 3:
mylr.alpha = 1.6e-4
mylr.max_iter = 200000
mylr.fit_(X, Y)
print(mylr.thetas)
# Output: array([[18.188..], [2.767..], [-0.374..], [1.392..], [0.017..]])
# Example 4:
y_hat = mylr.predict_(X)
print(y_hat)
# Output: array([[23.417..], [47.489..], [218.065...]])
# Example 5:
print(mylr.loss_elem_(Y, y_hat))
# Output: array([[0.174..], [0.260..], [0.004..]])
# Example 6:
print(mylr.loss_(Y, y_hat))
# Output: 0.0732..