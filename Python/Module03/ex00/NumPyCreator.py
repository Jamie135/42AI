import numpy as np

class NumPyCreator:

    def from_list(self, lst, dtype=None):
        # array(object, dtype=None, ...) return an array object satisfying the dtype specified
        try:
            return np.array(lst, dtype=dtype) if all(isinstance(lst, list) for i in lst) else None
        except:
            return None


    def from_tuple(self, tpl, dtype=None):
        try:
            return np.array(tpl, dtype=dtype) if isinstance(tpl, tuple) else None
        except:
            return None


    def from_iterable(self, itr, dtype=None):
        try:
            return np.array(list(itr), dtype=dtype)
        except:
            return None


    def from_shape(self, shape, value=0, dtype=None):
        # full(shape, fill_value, dtype=None, ...) returns a new array of given shape and dtype, filled with value
        try:
            return np.full(shape, value, dtype=dtype) if isinstance(shape, tuple) else None
        except:
            return None


    def random(self, shape, dtype=None):
        # random.random(size=None) return random floats in the half-open interval [0.0, 1.0(
        try:
            return np.random.random(shape).astype(dtype) if isinstance(shape, tuple) else None
        except:
            return None


    def identity(self, n, dtype=None):
        # eye(N, M=None, k=0, dtype=<class 'float'>, ...) returns a 2-D array with ones on the diagonal and zeros elsewhere
        try:
            return np.eye(n, dtype=dtype) if isinstance(n, int) else None
        except:
            return None
        

print("\n ########## TEST MANDATORY ##########\n")
# Example usage
npc = NumPyCreator()

print(npc.from_list([[1,2,3],[6,3,4]]))
# Output: array([[1, 2, 3], [6, 3, 4]])

print(npc.from_list([[1,2,3],[6,4]]))
# Output: None

print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
# Output: array([['1', '2', '3'], ['a', 'b', 'c'], ['6', '4', '7']], dtype='<U21')

print(npc.from_list(((1,2),(3,4))))
# Output: None

print(npc.from_tuple(("a", "b", "c")))
# Output: array(['a', 'b', 'c'])

print(npc.from_tuple(["a", "b", "c"]))
# Output: None

print(npc.from_iterable(range(5)))
# Output: array([0, 1, 2, 3, 4])

shape = (3, 5)
print(npc.from_shape(shape))
# Output: array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

print(npc.random(shape))
# Output: Random array with shape (3, 5)

print(npc.identity(4))
# Output: array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]])

print("\n ########## TEST BONUS ##########\n")
# Example usage
npc = NumPyCreator()

print(npc.from_list([[1, 2, 3], [6, 3, 4]], dtype=int))
# Output: array([[1, 2, 3], [6, 3, 4]])

print(npc.from_tuple((1.5, 2.5, 3.5), dtype=int))
# Output: array([1, 2, 3])

print(npc.from_iterable(range(5), dtype=float))
# Output: array([0., 1., 2., 3., 4.])

shape = (3, 5)
print(npc.from_shape(shape, value=7, dtype=int))
# Output: array([[7, 7, 7, 7, 7], [7, 7, 7, 7, 7], [7, 7, 7, 7, 7]])

print(npc.random(shape, dtype=float))
# Output: Random array with shape (3, 5) as floats

print(npc.identity(4, dtype=int))
# Output: array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
