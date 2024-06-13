import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import for 3D plotting


class KmeansClustering:
    
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids


    # method that runs K-means clustering algorithm on the dataset X
    def fit(self, X):

        # X is a numpy array representing the dataset with a shape of (m, n)
        # m is the number of data points and n is the number of features 
        # (in this case, n is 3 for height, weight, and bone_density)
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroid from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        # Step 1: Initialize centroids randomly from the dataset
        # random.choice() generates ncentroid amount 
        # of random indices from the range [0, X.shape[0]]
        # replace=Flase ensures that each centroid has a unique data point
        idx = np.random.choice(X.shape[0], self.ncentroid, replace=False)

        # X[idx] uses the array of indices idx to select the corresponding rows from X
        # self.centroids is a new numpy array containing the selected rows
        # which represent the initial centroids
        self.centroids = X[idx]


        for _ in range(self.max_iter):
            # Step 2: Assign points to the nearest centroid

            # clusters list of initially empty lists where each inner list 
            # will hold the points (index) assigned to a particular centroid
            clusters = [[] for _ in range(self.ncentroid)]
            for point in X:
                # compute the list of euclidean distances between the points and each centroids
                distances = np.linalg.norm(self.centroids - point, axis=1)
                # finds the index from distances of the centroid that is closest to the point
                cluster_idx = np.argmin(distances)
                clusters[cluster_idx].append(point)


            # Step 3: Update centroids to the mean of their assigned points
            for i in range(self.ncentroid):
                if clusters[i]:
                    self.centroids[i] = np.mean(clusters[i], axis=0)
        
    
    # method that assigns each data point to the nearest centroid based on the trained model
    # (i.e., the centroids found during the fit process)
    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        # zero() returns a numpy array labels of length m=X.shape[0] 
        # (number of data points) initialized with zeros
        labels = np.zeros(X.shape[0], dtype=int)
        for i, point in enumerate(X):
            # calculate distances to centroids
            distances = np.linalg.norm(self.centroids - point, axis=1)
            # find the nearest centroid
            labels[i] = np.argmin(distances)
        return labels
    

def main(filepath='../resources/solar_system_census.csv', ncentroid=4, max_iter=30):
    import sys
    # Check if command-line arguments are correctly provided
    if len(sys.argv) == 4:
        _, filepath, ncentroid, max_iter = sys.argv
        ncentroid = int(ncentroid)
        max_iter = int(max_iter)
    else:
        print("Usage: python Kmeans.py filepath='../resources/solar_system_census.csv' ncentroid=4 max_iter=30")
        return
    
    # Read the dataset
    data = pd.read_csv(filepath)

    # Extract relevant features (height, weight, bone_density)
    X = data[['height', 'weight', 'bone_density']].values

    # Initialize and fit K-means model
    kmeans = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)
    kmeans.fit(X)

    # Get cluster predictions
    labels = kmeans.predict(X)

    # Print centroids and associated regions
    for i, centroid in enumerate(kmeans.centroids):
        print(f"Centroid {i}: {centroid}")

    # Print number of individuals associated to each centroid
    for i in range(ncentroid):
        count = np.sum(labels == i)
        print(f"Individuals in cluster {i}: {count}")

    # Plotting the clusters
    if X.shape[1] == 3:  # Check if data is 3-dimensional for 3D plotting
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel('Height')
        ax.set_ylabel('Weight')
        ax.set_zlabel('Bone Density')

        # Plot data points
        ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels, cmap='viridis', label='Data Points')

        # Plot centroids
        ax.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], kmeans.centroids[:, 2],
                   marker='x', s=100, c='r', label='Centroids')

        plt.title('K-means Clustering')
        plt.legend()
        plt.show()
    else:
        print("Cannot plot data with dimensions other than 3.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 4:
        _, filepath, ncentroid, max_iter = sys.argv
        main(filepath, int(ncentroid), int(max_iter))
    else:
        print("Usage: python Kmeans.py filepath='../resources/solar_system_census.csv' ncentroid=4 max_iter=30")
