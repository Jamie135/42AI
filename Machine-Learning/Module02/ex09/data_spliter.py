import numpy as np


def data_spliter(x, y, proportion):
    """Shuffles and splits the dataset (given by x and y) into a training and a test set,
    while respecting the given proportion of examples to be kept in the training set.
    Args:
    x: has to be an numpy.array, a matrix of dimension m * n.
    y: has to be an numpy.array, a vector of dimension m * 1.
    proportion: has to be a float, the proportion of the dataset that will be assigned to the
    training set.
    Return:
    (x_train, x_test, y_train, y_test) as a tuple of numpy.array
    None if x or y is an empty numpy.array.
    None if x and y do not share compatible dimensions.
    None if x, y or proportion is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        return None
    m = x.shape[0]
    n = x.shape[1]
    if m == 0 or n == 0:
        return None
    elif y.shape != (m, 1):
        return None
    if not isinstance(proportion, (int, float)):
        return None
    elif proportion < 0.0 or proportion > 1.0:
        return None
    
    indices = np.random.permutation(m)
    x_shuffled = x[indices]
    y_shuffled = y[indices]
    
    # Determine the split index
    split_idx = int(m * proportion)
    
    # Split the dataset
    x_train = x_shuffled[:split_idx]
    x_test = x_shuffled[split_idx:]
    y_train = y_shuffled[:split_idx]
    y_test = y_shuffled[split_idx:]
    
    return x_train, x_test, y_train, y_test


if __name__ == "__main__":
    x1 = np.array([1, 42, 300, 10, 59]).reshape((-1, 1))
    y1 = np.array([0, 1, 0, 1, 0]).reshape((-1, 1))

    x_train, x_test, y_train, y_test = data_spliter(x1, y1, 0.8)
    print("X_train:", x_train.flatten())
    print("X_test:", x_test.flatten())
    print("y_train:", y_train.flatten())
    print("y_test:", y_test.flatten())

    x2 = np.array([[1, 42], [300, 10], [59, 1], [300, 59], [10, 42]])
    y2 = np.array([0, 1, 0, 1, 0]).reshape((-1, 1))

    x_train, x_test, y_train, y_test = data_spliter(x2, y2, 0.5)
    print("X_train:", x_train)
    print("X_test:", x_test)
    print("y_train:", y_train.flatten())
    print("y_test:", y_test.flatten())
