import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


class MyLinearRegression():

    """
    Description:
    My personnal linear regression class to fit like a boss.
    """

    def __init__(self, thetas, alpha=0.0001, max_iter=500_000):
        if not isinstance(alpha, float) or alpha < 0.0:
            return None
        elif not isinstance(max_iter, int) or max_iter < 0:
            return None
        self.thetas = np.array(thetas)
        self.alpha = alpha
        self.max_iter = max_iter


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
        if not isinstance(x, np.ndarray):
            return None
        elif x.size == 0:
            return None
        m = x.shape[0]
        n = x.shape[1]
        if self.thetas.shape != (n + 1, 1):
            return None
        # Add a column of ones to x to account for theta0
        X_prime = np.c_[np.ones(m), x]
        return X_prime @ self.thetas


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
        elif self.thetas.shape != (n + 1, 1):
            return None
        X_prime = np.c_[np.ones(m), x]
        return (X_prime.T @ (X_prime @ self.thetas - y)) / m


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
        elif self.thetas.shape != ((n + 1), 1):
            return None
        for _ in self.ft_progress(range(self.max_iter)):
            gradient = self.gradient_(x, y)
            if gradient is None:
                return None
            if all(__ == 0. for __ in gradient):
                break
            self.thetas -= self.alpha * gradient
        return self.thetas


    def mse_elem(self, y, y_hat) -> np.ndarray:
        return (y_hat - y) ** 2


    def mse_(self, y, y_hat) -> float:
        if any(not isinstance(_, np.ndarray) for _ in [y, y_hat]):
            return None
        m = y.shape[0]
        if m == 0 or y.shape != (m, 1) or y_hat.shape != (m, 1):
            return None
        J_elem = self.mse_elem(y, y_hat)
        return J_elem.mean()


    def minmax(x):
        if not isinstance(x, np.ndarray):
            return None
        if x.size == 0:
            return None
        if x.ndim != 1:
            x = x.reshape(-1)
        return (x - np.min(x)) / (np.max(x) - np.min(x))
    

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


    def add_polynomial_features(self, x, power):
        """Add polynomial features to vector x by raising its values up to the power given in argument.
        Args:
        x: has to be an numpy.array, a vector of dimension m * 1.
        power: has to be an int, the power up to which the components of vector x are going to be raised.
        Return:
        The matrix of polynomial features as a numpy.array, of dimension m * n,
        containing the polynomial feature values for all training examples.
        None if x is an empty numpy.array.
        None if x or power is not of expected type.
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(x, np.ndarray) or not isinstance(power, int):
            return None
        elif x.size == 0 or power < 0:
            return None
        if power == 0:
            return np.ones((x.size, 1))
        res = np.ones((x.size, power))
        for i in range(power):
            res[:, i] = x.ravel() ** (i + 1)
        return res


if __name__ == "__main__":
    linear_regression = MyLinearRegression([80, -10], 10e-10, 100_000)
    try:
        data = pd.read_csv("./are_blue_pills_magics.csv")
    except FileExistsError:
        print("File not found")

    x = data['Micrograms'].values
    y = data['Score'].values.reshape(-1, 1)

    polynom = linear_regression.add_polynomial_features(x, 6)

    theta1 = np.array([[89.04720427],
                        [-8.99425854]]
                        ).reshape(-1, 1)

    theta2 = np.array([[69.77316037],
                        [1.49660362],
                        [-1.21861482]]).reshape(-1, 1)

    theta3 = np.array([[89.0],
                        [-8.4],
                        [0.8],
                        [-0.1]]).reshape(-1, 1)

    theta4 = np.array([[-20.0],
                        [160.0],
                        [-80.0],
                        [10.0],
                        [-1.0]]
                        ).reshape(-1, 1)

    theta5 = np.array([[1140],
                        [-1850],
                        [1110],
                        [-305],
                        [40.0],
                        [-2.0]]
                        ).reshape(-1, 1)

    theta6 = np.array([[9110],
                        [-18015],
                        [13400],
                        [-4935],
                        [966],
                        [-96.4],
                        [3.86]]
                        ).reshape(-1, 1)

    hypothesis_thetas = [theta1, theta2, theta3, theta4, theta5, theta6]

    thetas = []
    mse_scores = []

    # Trains six separate Linear Regression models with polynomial
    # hypothesis with degrees ranging from 1 to 6
    # Plots the 6 models and the data points on the same figure.
    # Use lineplot style for the models and scaterplot for the data points.
    # Add more prediction points to have smooth curves for the models.
    fig, ax = plt.subplots(2, 3)

    for i in range(1, 7):
        print("Training model {} / 6\n".format(i))

        linear_regression.thetas = hypothesis_thetas[i - 1]
        current_x = polynom[:, :i]
        linear_regression.fit_(current_x, y)
        y_hat = linear_regression.predict_(current_x)

        thetas.append(linear_regression.thetas)
        mse_scores.append(linear_regression.mse_(y, y_hat))

        # Plots the data points
        ax[(i - 1) // 3][(i - 1) % 3].scatter(x, y, color='blue')

        # Plots the model curve
        min_x = np.min(x)
        max_x = np.max(x)
        continuous_x = np.linspace(min_x, max_x, 100)
        predicted_x = linear_regression.add_polynomial_features(continuous_x,
                                                                i)
        predicted_y = linear_regression.predict_(predicted_x)
        ax[(i - 1) // 3][(i - 1) % 3].plot(continuous_x, predicted_y, color='orange')
        # Add title and axis names
        ax[(i - 1) // 3][(i - 1) % 3].set_title("Degree {}, score : {}".format(i, mse_scores[i - 1]))
        ax[(i - 1) // 3][(i - 1) % 3].set_xlabel("Micrograms")
        ax[(i - 1) // 3][(i - 1) % 3].set_ylabel("Score")

        # Compute Loss
        loss = linear_regression.loss_(y, y_hat)
        print()
        print("Loss {} : {}".format(i, loss))
        print("Thetas : {}".format(linear_regression.thetas))
        print()

    plt.show()

    for i in range(6):
        print("Model {} :".format(i + 1))
        print("Thetas : {}".format(thetas[i]))
        print("MSE : {}\n".format(mse_scores[i]))

    # Plots a bar plot showing the MSE score of the models in function of
    # the polynomial degree of the hypothesis,
    plt.bar([1, 2, 3, 4, 5, 6], mse_scores)
    plt.xlabel("Polynomial degree")
    plt.ylabel("MSE")
    plt.show()
