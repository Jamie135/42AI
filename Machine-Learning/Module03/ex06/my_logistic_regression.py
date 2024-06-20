import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


class MyLogisticRegression():

    """
    Description:
    My personnal logistic regression class to classify things.
    """

    def __init__(self, theta, alpha=0.001, max_iter=1000):
        self.theta = theta
        self.alpha = alpha
        self.max_iter = max_iter


    @staticmethod
    def sigmoid_(x):
        """
        Compute the sigmoid of a vector.
        Args:
        x: has to be a numpy.ndarray of shape (m, 1).
        Returns:
        The sigmoid value as a numpy.ndarray of shape (m, 1).
        None if x is an empty numpy.ndarray.
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(x, np.ndarray):
            return None
        if x.shape[0] == 0 or x.shape[1] != 1:
            return None
        e = np.exp(-x)
        return 1 / (1 + e)


    def predict_(self, x):
        """
        Computes the vector of prediction y_hat from two
        non-empty numpy.ndarray.
        Args:
        x: has to be an numpy.ndarray, a vector of dimension m * n.
        Returns:
        y_hat as a numpy.ndarray, a vector of dimension m * 1.
        None if x or theta are empty numpy.ndarray.
        None if x or theta dimensions are not appropriate.
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(x, np.ndarray):
            return None
        m = x.shape[0]
        n = x.shape[1]
        if m == 0 or n == 0 or self.theta.shape != (n + 1, 1):
            return None
        # Add a column of ones to x to account for theta0
        X0 = np.c_[np.ones(m), x]
        y_hat = self.sigmoid_(X0 @ self.theta)
        return y_hat


    def gradient_(self, x, y):
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
        for array in [x, y]:
            if not isinstance(array, np.ndarray):
                return None
        m, n = x.shape
        if m == 0 or n == 0:
            return None
        elif y.shape != (m, 1):
            return None
        elif self.theta.shape != (n + 1, 1):
            return None
        
        X_prime = np.c_[np.ones(m), x]
        y_hat = self.predict_(x)
        if y_hat is None:
            return None
        return (X_prime.T @ (y_hat - y)) / m


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
        for arr in [x, y]:
            if not isinstance(arr, np.ndarray):
                return None
        m, n = x.shape
        if m == 0 or n == 0:
            return None
        if y.shape != (m, 1):
            return None
        elif self.theta.shape != ((n + 1), 1):
            return None
        for _ in self.ft_progress(range(self.max_iter)):
            gradient = self.gradient_(x, y)
            if gradient is None:
                return None
            if all(__ == 0. for __ in gradient):
                break
            self.theta -= self.alpha * gradient
        return self.theta


    def loss_elem_(self, y, y_hat, eps=1e-15):
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
        m, n = y.shape
        if y.shape != y_hat.shape or m == 0 or n == 0:
            return None

        y_hat = np.clip(y_hat, eps, 1 - eps)

        J_elem = []
        for y_value, y_hat_value in zip(y, y_hat):
            loss = -((y_value * np.log(y_hat_value)) + ((1 - y_value) * np.log(1 - y_hat_value)))
            J_elem.append(loss)
        return J_elem
    

    def loss_(self, y, y_hat, eps=1e-15):
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
        J_elem = self.loss_elem_(y, y_hat, eps)
        if J_elem is None:
            return None
        return np.mean(J_elem)
    

    def ft_progress(self, iterable):
        total = len(iterable)
        start_time = time.time()
        # enumerate parcour iterable tout en gardant une trace de l'index de chaque élément
        for i, val in enumerate(iterable):
            # val represente l'element actuel de iterable
            # yield val sert à retourner l'élément de iterable sans terminer la fonction
            # elle renvoie un résultat au générateur appelant et conserve l'état de la fonction 
            # pour que l'exécution puisse reprendre là où elle s'est arrêtée lors du prochain appel 
            yield val

            # proportion de la barre parcourue
            progress = i / total

            # le temps écoulé depuis le début de l'itération
            elapsed_time = time.time() - start_time

            # calcul pour l'estimation du temps restant
            if progress > 0:
                eta = elapsed_time / progress * (1 - progress)
            else:
                eta = 0

            # '=' * int(progress * 20) calcule le nombre de symboles '='
            # ' ' * (19 - int(progress * 20)) calcule le nombre d'espaces nécessaires pour compléter la barre
            progress_bar = '[' + '=' * int(progress * 20) + '>' + ' ' * (19 - int(progress * 20)) + ']'

            # affiche la progression de la barre formatté comme dans le sujet
            #'\r' permet de overwrite la ligne recente de la progression
            print(f"ETA: {eta:.2f}s [{int(progress * 100)}%]{progress_bar} {i}/{total} | elapsed time {elapsed_time:.2f}s", end='\r')
        print()


# Testing the class with the provided examples
if __name__ == "__main__":
    X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [3., 5., 9., 14.]])
    Y = np.array([[1], [0], [1]])
    theta = np.array([[2], [0.5], [7.1], [-4.3], [2.09]])
    
    mylr = MyLogisticRegression(theta)
    
    # Example 0:
    print("Example 0:", mylr.predict_(X))
    # Output:
    # array([[0.99930437],
    # [1. ],
    # [1. ]])
    
    # Example 1:
    print("Example 1:", mylr.loss_(Y, mylr.predict_(X)))
    # Output: 11.513157421577002
    
    # Example 2:
    mylr.fit_(X, Y)
    print("Example 2:", mylr.theta)
    # Output:
    # array([[ 2.11826435]
    # [ 0.10154334]
    # [ 6.43942899]
    # [-5.10817488]
    # [ 0.6212541 ]])
    
    # Example 3:
    print("Example 3:", mylr.predict_(X))
    # Output:
    # array([[0.57606717]
    # [0.68599807]
    # [0.06562156]])
    
    # Example 4:
    print("Example 4:", mylr.loss_(Y, mylr.predict_(X)))
    # Output: 1.4779126923052268
