class Matrix:

    def __init__(self, arg):
        if isinstance(arg, list):
            self.data = arg
            self.shape = (len(arg), len(arg[0]))
        elif isinstance(arg, tuple):
            row, col = arg
            for _ in range (row):
                self.data = [[0.0] * col]
            self.shape = arg
        else:
            raise ValueError("Invalid input")


    def __add__(self, mat):
        if not isinstance(mat, Matrix) or self.shape != mat.shape:
            raise ValueError("Addition requires two matrices of the same dimensions.")
        result = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.data[i][j] + mat.data[i][j])
            result.append(row)
        return Matrix(result)
    

    def __radd__(self, mat):
        return self.__add__(mat)
    

    def __sub__(self, mat):
        if not isinstance(mat, Matrix) or self.shape != mat.shape:
            raise ValueError("Substraction requires two matrices of the same dimensions.")
        result = [
            [self.data[row][col] - mat.data[row][col] for col in range(self.shape[1])]
            for row in range(self.shape[0])
        ]
        return Matrix(result)
    

    def __rsub__(self, mat):
        return self.__sub__(mat)
    

    def __truediv__(self, scalar):
        if not isinstance(scalar, (float, int)):
            raise ValueError("Division requires a scalar (float or int).")
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = [
            [self.data[row][col] / scalar for col in range(self.shape[1])]
            for row in range(self.shape[0])
            ]
        return Matrix(result)
    

    def __rtruediv__(self, scalar):
        raise ArithmeticError("Division of a scalar by a vector is not defined.")
    

    def __mul__(self, arg):
        if isinstance(arg, (float, int)):
            result = [
                [self.data[row][col] * arg for col in range(self.shape[1])]
                for row in range(self.shape[0])
                ]
        elif isinstance(arg, Matrix):
            if self.shape[1] != arg.shape[0]:
                raise ValueError("Matrix dimensions do not match for multiplication.")
            result = [
                [sum(a * b for a, b in zip(self_row, arg_col)) for arg_col in zip(*arg.data)]
                for self_row in self.data
            ]
        else:
            raise ValueError("Unsupported operand type(s) for multiplication")  
        return Matrix(result)
    

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.__mul__(other)
        else:
            raise ValueError("Unsupported operand type(s) for multiplication")


    def __str__(self):
        return f"Matrix({self.data})"
    

    def __repr__(self):
        return f"Matrix({self.data})"
    

    def T(self):
        # result = []
        # for i in range(self.shape[1]):
        #     row = []
        #     for j in range(self.shape[0]):
        #         row.append(self.data[j][i])
        #     result.append(row)
        result = [list(row) for row in zip(*self.data)]
        return Matrix(result)


class Vector(Matrix):

    def __init__(self, arg):
        super().__init__(arg)
        if not (self.shape[0] == 1 or self.shape[1] == 1):
            raise ValueError("Invalid input")
    

    def dot(self, vect):
        if not isinstance(vect, Vector):
            raise ValueError("Invalid input")
        if self.shape[1] != vect.shape[0] and self.shape[0] != vect.shape[1]:
            raise ValueError("Shapes do not match for dot product.")
        res = 0
        # row
        if self.shape[0] == 1:
            for a, b in zip(self.data[0], vect.data[0]):
                res += a * b
        # column
        else:
            for a, b in zip(self.data, vect.data):
                res += a[0] * b[0]
        return res
    

    def __repr__(self):
        return f"Vector({self.data})"
