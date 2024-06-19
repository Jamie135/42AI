import numpy as np

class MyLinearRegression():
    """
    Description:
    My personnal linear regression class to fit like a boss.
    """

    def __init__(self, thetas, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    @staticmethod
    def simple_gradient(x, y, thetas):
        """Computes a gradient vector from three non-empty numpy.array, with a for-loop.
        The three arrays must have compatible shapes.
        Args:
        x: has to be an numpy.array, a vector of shape m * 1.
        y: has to be an numpy.array, a vector of shape m * 1.
        thetas: has to be an numpy.array, a 2 * 1 vector.
        Return:
        The gradient as a numpy.array, a vector of shape 2 * 1.
        None if x, y, or thetas are empty numpy.array.
        None if x, y and thetas do not have compatible shapes.
        None if x, y or thetas is not of the expected type.
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(thetas, np.ndarray):
            return None
        if x.size == 0 or y.size == 0 or thetas.size == 0:
            return None
        if x.shape[0] != y.shape[0] or thetas.shape != (2, 1):
            return None
        
        m = x.shape[0]
        # add a column of ones to x to create a matrix X0
        X0 = np.hstack((np.ones((m, 1)), x))
        # with X0 as a matrix, we can now use vectorization instead of for loop
        # to calculate the error array and use error to calculate the gradient array
        error = np.dot(X0, thetas) - y
        # .T is a method to transpose a matrix
        gradient = np.dot(X0.T, error) / m
        return gradient


    def fit_(self, x, y):
        """
        Description:
        Fits the model to the training dataset contained in x and y.
        Args:
        x: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
        y: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
        thetas: has to be a numpy.ndarray, a vector of dimension 2 * 1.
        alpha: has to be a float, the learning rate
        max_iter: has to be an int, the number of iterations done during the gradient descent
        Returns:
        new_thetas: numpy.ndarray, a vector of dimension 2 * 1.
        None if there is a matching dimension problem.
        Raises:
        This function should not raise any Exception.
        """
        if x.ndim != 2 or y.ndim != 2 or self.thetas.ndim != 2 or x.shape[1] != 1 or y.shape[1] != 1 or self.thetas.shape != (2, 1):
            return None
        for _ in range(self.max_iter):
            gradient = self.simple_gradient(x, y, self.thetas)
            self.thetas = self.thetas - self.alpha * gradient
        return self.thetas
    
    
    def predict_(self, x):
        """
        Computes the vector of prediction y_hat from two non-empty numpy.array.
        Args:
        x: has to be an numpy.array, a one-dimensional array of size m.
        thetas: has to be an numpy.array, a two-dimensional array of shape 2 * 1.
        Returns:
        y_hat as a numpy.array, a two-dimensional array of shape m * 1.
        None if x and/or thetas are not numpy.array.
        None if x or thetas are empty numpy.array.
        None if x or thetas dimensions are not appropriate.
        Raises:
        This function should not raise any Exceptions.
        """
        if not isinstance(x, np.ndarray) or not isinstance(self.thetas, np.ndarray):
            return None
        if x.ndim != 2 or self.thetas.ndim != 2 or self.thetas.shape != (2, 1):
            return None
        
        X0 = np.c_[np.ones((x.shape[0], 1)), x]
        y_hat = np.dot(X0, self.thetas)
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
        if y.shape != y_hat.shape:
            return None
        if y.ndim != 2 or y.shape[1] != 1:
            return None

        J_elem = (y_hat - y) ** 2
        return J_elem
    

    def loss_(self, y, y_hat):
        """
        Description:
        Calculates the value of loss function.
        Args:
        y: has to be an numpy.array, a two-dimensional array of shape m * 1.
        y_hat: has to be an numpy.array, a two-dimensional array of shape m * 1.
        Returns:
        J_value : has to be a float.
        None if there is a dimension matching problem.
        None if any argument is not of the expected type.
        Raises:
        This function should not raise any Exception.
        """
        J = self.loss_elem_(y, y_hat)
        if J is None:
            return None
        return np.mean(J) / 2


x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
lr1 = MyLinearRegression(np.array([[2], [0.7]]))

# Example 0.0:
y_hat = lr1.predict_(x)
print(f"\nExample 0.0: {y_hat}\n")
# Output:
# array([[10.74695094],
# [17.05055804],
# [24.08691674],
# [36.24020866],
# [42.25621131]])
# Example 0.1:
print(f"\nExample 0.1: {lr1.loss_elem_(y, y_hat)}\n")
# Output:
# array([[710.45867381],
# [364.68645485],
# [469.96221651],
# [108.97553412],
# [299.37111101]])
# Example 0.2:
print(f"\nExample 0.2: {lr1.loss_(y, y_hat)}\n")
# Output: 195.34539903032385

# Example 1.0:
lr2 = MyLinearRegression(np.array([[1], [1]]), 5e-8, 1500000)
lr2.fit_(x, y)
print(f"\nExample 1.0: {lr2.thetas}\n")
# Output:
# array([[1.40709365],
# [1.1150909 ]])

# Example 1.1:
y_hat = lr2.predict_(x)
print(f"\nExample 1.1: {y_hat}\n")
# Output:
# array([[15.3408728 ],
# [25.38243697],
# [36.59126492],
# [55.95130097],
# [65.53471499]])

# Example 1.2:
print(f"\nExample 1.2: {lr2.loss_elem_(y, y_hat)}\n")
# Output:
# array([[486.66604863],
# [115.88278416],
# [ 84.16711596],
# [ 85.96919719],
# [ 35.71448348]])

# Example 1.3:
print(f"\nExample 1.3: {lr2.loss_(y, y_hat)}\n")
# Output: 80.83996294128525
