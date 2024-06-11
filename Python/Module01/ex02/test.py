from vector import Vector

# SUBJECT TEST #
print("\n########### SUBJECT TEST ###########\n")
try:
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 * 5
    print(v2)

    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 * 5
    print(v2)

    v2 = v1 / 2.0
    print(v2)

    # v1 / 0.0

    # 2.0 / v1

    print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)

    print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)

    print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)

    print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)

    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.shape)

    (4,1)
    print(v1.T())

    print(v1.T().shape)

    v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v2.shape)

    print(v2.T())

    print(v2.T().shape)

    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print(v1.dot(v2))

    v3 = Vector([[1.0, 3.0]])
    v4 = Vector([[2.0, 4.0]])
    print(v3.dot(v4))

    v1
    print(v1)
    
except Exception as e:
    print(e)
print("\n")


# MYTEST #
print("########### MY TEST ###########\n")
def test_operations():
    # Test addition and subtraction for row vectors
    v1 = Vector([[1., 2., 3.]])
    v2 = Vector([[4., 5., 6.]])
    print((v1 + v2).values == [[5., 7., 9.]])
    print((v1 - v2).values == [[-3., -3., -3.]])

    # Test addition and subtraction for column vectors
    v3 = Vector([[1.], [2.], [3.]])
    v4 = Vector([[4.], [5.], [6.]])
    print((v3 + v4).values == [[5.], [7.], [9.]])
    print((v3 - v4).values == [[-3.], [-3.], [-3.]])

    # Test multiplication and division by scalar
    scalar = 2
    print((v1 * scalar).values == [[2., 4., 6.]])
    print((scalar * v1).values == [[2., 4., 6.]])
    print((v3 * scalar).values == [[2.], [4.], [6.]])
    print((scalar * v3).values == [[2.], [4.], [6.]])

    print((v1 / scalar).values == [[0.5, 1.0, 1.5]])
    print((v3 / scalar).values == [[0.5], [1.0], [1.5]])

    # Test dot product for row vectors
    print(v1.dot(v2) == 32.0)

    # Test dot product for column vectors
    print(v3.dot(v4) == 32.0)

    # Test transpose
    print(v1.T().values == [[1.], [2.], [3.]])
    print(v3.T().values == [[1., 2., 3.]])

    # Test division by zero
    try:
        v1 / 0
    except ZeroDivisionError:
        print("Caught division by zero")

    # Test division of scalar by vector
    try:
        2 / v1
    except ArithmeticError:
        print("Caught arithmetic error")

if __name__ == "__main__":
    test_operations()
    print("Done!")

