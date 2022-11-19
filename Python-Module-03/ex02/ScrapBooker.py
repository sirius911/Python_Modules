import numpy as np

class ScrapBooker:
    """Manipulation and initiation to slicing method on numpy arrays."""
    def __init__(self) -> None:
        pass

    def crop(self, array:np.array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Return:
        -------
            new_arr: the cropped numpy.ndarray.
            None (if combinaison of parameters not compatible).
        Raise:
        ------
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) and isinstance(dim, tuple)\
             and isinstance(position, tuple):
            try:
                start_row = position[0]
                end_row = start_row + dim[0]
                start_col = position[1]
                end_col = start_col + dim[1]
                if start_row < array.shape[0] and end_row < array.shape[0]\
                and start_col < array.shape[1] and end_col < array.shape[1]:
                    return np.array(array[start_row:end_row, start_col:end_col])
            except Exception as e:
                return None
        return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column of the array(depending of axis value).
            axis: positive non null integer.
        Return:
        -------
            new_arr: thined numpy.ndarray.
            None (if combinaison of parameters not compatible).
        Raise:
        ------
            This function should not raise any Exception.
        """
        ret = None
        if isinstance(array, np.ndarray) and isinstance(axis, int)\
            and axis in range(0,2) and isinstance(n, int) and n > 0:
            axis = 1 - axis     # inversion mais je ne suis pas d'accord avec le sujet !!!
            max=array.shape[axis]
            ret = np.delete(array, list(range(n-1, max, n)), axis=axis)
        return ret

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Return:
        -------
            new_arr: juxtaposed numpy.ndarray.
            None (combinaison of parameters not compatible).
        Raises:
        -------
            This function should not raise any Exception.
        """
        ret = None
        if isinstance(array, np.ndarray) and isinstance(n, int) and n > 0\
            and isinstance(axis, int) and axis in range(0,2):
            ret = array
            if axis == 1:
                for _ in range(n-1):
                    ret = np.hstack((ret, array))
            else:
                for _ in range(n - 1):
                    ret = np.vstack((ret, array))
        return np.array(ret)

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
            array: numpy.ndarray.
            dim: tuple of 2 integers.
        Return:
        -------
            new_arr: mosaic numpy.ndarray.
            None (combinaison of parameters not compatible).
        Raises:
        -------
            This function should not raise any Exception.
        """

        ret = None
        if isinstance(array, np.ndarray)  and isinstance(dim, tuple):
            a, b = dim
            if isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0:
                ret = self.juxtapose(array, a, 0)
                ret = self.juxtapose(ret, b, 1)
        return np.array(ret)

