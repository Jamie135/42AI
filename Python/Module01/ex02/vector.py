class Vector:

    def __init__(self, values):
        # check type for values
        if not isinstance(values, list):
            raise TypeError("Values must be a list of lists of floats/integers.")
        for i in values:
            for j in i:
                if not isinstance(i, list) or not isinstance(j, (float, int)):
                    raise TypeError("Values must be a list of lists of floats/integers.")
        self.values = values

        # assign the shape
        if len(values) == 1:
            self.shape = (1, len(values[0]))
        else:
            self.shape = (len(values), 1)
        
        # check if all rows have same number of element
        for row in values:
            if not (len(row) == self.shape[1]):
                raise ValueError("All rows must have the same number of elements.")


    def dot(self, vect):
        if not isinstance(vect, Vector) or self.shape != vect.shape:
            raise ValueError("Dot product requires two vectors of the same shape.")
        
        res = 0
        # row
        if self.shape[0] == 1:
            # zip() method merges passed lists into one
            # by combining the values at the same index of both list in a tuple
            for a, b in zip(self.values[0], vect.values[0]):
                res += a * b
        # column
        else:
            for a, b in zip(self.values, vect.values):
                res += a[0] * b[0]
        return res


    def T(self):
        if self.shape[0] == 1:
            return Vector([[v] for v in self.values[0]])
        else:
            return Vector([[v[0] for v in self.values]])


    def __repr__(self):
        return str(self.values)


    def __str__(self):
        return str(self.values)
    

    def __add__(self, vect):
        if not isinstance(vect, Vector) or self.shape != vect.shape:
            raise ValueError("Addition requires two vectors of the same shape.")
        
        if self.shape[0] == 1:
            return Vector([[a + b for a, b in zip(self.values[0], vect.values[0])]])
        else:
            return Vector([[a[0] + b[0]] for a, b in zip(self.values, vect.values)])


    def __sub__(self, vect):
        if not isinstance(vect, Vector) or self.shape != vect.shape:
            raise ValueError("Subtraction requires two vectors of the same shape.")
        
        if self.shape[0] == 1:
            return Vector([[a - b for a, b in zip(self.values[0], vect.values[0])]])
        else:
            return Vector([[a[0] - b[0]] for a, b in zip(self.values, vect.values)])


    def __mul__(self, scalar):
        if not isinstance(scalar, (float, int)):
            raise ValueError("Multiplication requires a scalar (float or int).")
        
        if self.shape[0] == 1:
            return Vector([[a * scalar for a in self.values[0]]])
        else:
            return Vector([[a[0] * scalar] for a in self.values])


    def __rmul__(self, scalar):
        return self.__mul__(scalar)


    def __truediv__(self, scalar):
        if not isinstance(scalar, (float, int)):
            raise ValueError("Division requires a scalar (float or int).")
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        
        if self.shape[0] == 1:
            return Vector([[a / scalar for a in self.values[0]]])
        else:
            return Vector([[a[0] / scalar] for a in self.values])


    def __rtruediv__(self, scalar):
        raise ArithmeticError("Division of a scalar by a vector is not defined.")
