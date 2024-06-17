from matrix import Matrix, Vector

m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
m2 = Matrix([[2.0, 0.0], [1.0, 2.0]])

v1 = Vector([[1, 2, 3]])  # Row vector
v2 = Vector([[1], [2], [3]])  # Column vector

print(m1.shape)
print(2 * m1)
print(m2 * 4)
print(m1 - m2)
print(m1 * m2)

# This should raise an error
try:
    v3 = Vector([[1, 2], [3, 4]])  # Invalid vector
except ValueError as e:
    print(e)  # Output: Invalid input

# Dot product of vectors
dot_product = v1.dot(v2)
print(dot_product)  # Output: 14

# Transpose example
m3 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
print(m1.T())  # Output: Matrix([[0.0, 2.0, 4.0], [1.0, 3.0, 5.0]])

# Matrix and vector multiplication
m4 = Matrix([[0.0, 1.0, 2.0], [0.0, 2.0, 4.0]])
v3 = Vector([[1], [2], [3]])
result = m4 * v3
print(result)