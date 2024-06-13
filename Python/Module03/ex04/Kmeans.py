import numpy as np
import pandas as pd


class KmeansClustering:
    
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids


    def fit(self, X):
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
        idx = np.random.choice(X.shape[0], self.ncentroid, replace=False)
        self.centroids = X[idx]

        for _ in range(self.max_iter):
            # Step 2: Assign points to the nearest centroid
            clusters = [[] for _ in range(self.ncentroid)]
            for point in X:
                distances = np.linalg.norm(self.centroids - point, axis=1)
                cluster_idx = np.argmin(distances)
                clusters[cluster_idx].append(point)

            # Step 3: Update centroids to the mean of their assigned points
            for i in range(self.ncentroid):
                if clusters[i]:
                    self.centroids[i] = np.mean(clusters[i], axis=0)
        
    
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
        labels = np.zeros(X.shape[0], dtype=int)
        for i, point in enumerate(X):
            distances = np.linalg.norm(self.centroids - point, axis=1)
            labels[i] = np.argmin(distances)
        return labels
    

def main(filepath='../resources/solar_system_census.csv', ncentroid=4, max_iter=30):
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

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 4:
        _, filepath, ncentroid, max_iter = sys.argv
        main(filepath, int(ncentroid), int(max_iter))
    else:
        print("Usage: python Kmeans.py filepath='../resources/solar_system_census.csv' ncentroid=4 max_iter=30")
