import numpy as np

class NumPyCreator:
    """Class implemented many methods who returns different type of sata structure into
    a Numpy array"""

    def __init__(self):
        """initialisation"""
        self.array = None

    def from_list(self, lst):
        """takes a list or nested lists and returns its corresponding Numpy array."""
        self.array = None
        if type(lst) is list:
            self.array = np.array(lst)
            if self.array.dtype == np.object:
                self.array = None
        return self.array

    def from_tuple(self, tpl):
        """takes a tuple or nested tuples and returns its corresponding Numpy array."""
        self.array = None
        if type(tpl) is tuple:
            self.array = np.array(tpl)
        return self.array

    def from_iterable(self, itr):
        """akes an iterable and returns an array which contains all its elements."""
        self.array = np.empty(len(itr))
        index = np.arange(self.array.size)
        np.put(self.array, index, itr)
        return self.array

    def from_shape(self, shape, value = 0):
        """returns an array filled with the same value.
            The first argument is a tuple which specifies the shape of the array,
            and the second argument specifies the value of the elements.
            This value must be 0 by default."""
        self.array = np.full(shape, value)
        return self.array

    def random(self, shape):
        """returns an array filled with random values. It takes as an argument a tuple which specifies the shape of the array.
        """
        self.array = None
        if type(shape) is tuple:
            a, b = shape
            self.array = np.random.rand(a, b)
        return self.array

    def identity(self, n):
        """returns an array representing the identity matrix of size n."""
        self.array = None
        if isinstance(n, int):
            self.array = np.identity(n)
        return self.array