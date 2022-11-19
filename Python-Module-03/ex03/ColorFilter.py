import math
from xmlrpc.client import boolean
import numpy as np

class ColorFilter():
    """Class to manipulate color's filter of image with ndArray"""
    def __init__(self) -> None:
        pass

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            ret = array.copy()
            if ret.dtype == np.float32:   # to cast in int
                ret = (ret * 255).astype(np.uint8)
            if array.shape[2] == 3:
                ret = 255 - ret
            else:
                ret[:,:,(0,1,2)] = 255 - ret[:,:,(0,1,2)]
            return ret
        return None

    def to_blue(self, array):
        """
        Applies a blue filter to
        the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            ret = array.copy()
            ret[:,:,(0,1)] = 0  # we put the first(R) and Second(G) to 0
            return ret
        return None

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
         None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            ret = array.copy()
            ret[:,:,(0,2)] = 0  # we put the first(R) and third(B) to 0
            return ret
        return None

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            ret = array.copy()
            ret[:,:,(1,2)] = 0  # we put the second(G) and third(B) to 0
            return ret
        return None

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        num_colors = 4

        if isinstance(array, np.ndarray):
            ret = array.copy()
            alpha_channel =  (array.shape[2] == 4)
            for i in range(len(ret)):
                for j in range(len(ret[i])):
                    if alpha_channel:
                        r, g, b, a = ret[i, j]
                    else:
                        r, g, b = ret[i, j]
                    r = math.floor(r * num_colors + 0.5) / num_colors
                    g = math.floor(g * num_colors + 0.5) / num_colors
                    b = math.floor(b * num_colors + 0.5) / num_colors
                    if alpha_channel:
                        ret[i, j] = (r, g, b, a)
                    else:
                        ret[i, j] = (r, g, b)
            return ret
        return None

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
            For filter = ’mean’/’m’: performs the mean of RBG channels.
            For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
            weights: [kwargs] list of 3 floats where the sum equals to 1,
                corresponding to the weights of each RBG channels.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        use_alpha = kwargs.get('alpha', True) # True to save Alpha Channel

        if isinstance(array, np.ndarray) and isinstance(filter, str)\
            and filter in ['m', 'mean', 'w', 'weight']:
            if use_alpha is False:
                ret = array[:,:,:3].copy() # to delete Alpha Channel
            else:
                ret = array.copy()
            alpha_channel =  (ret.shape[2] == 4)
            if ret.dtype == np.float32:   # to cast in int
                ret = (ret * 255).astype(np.uint8)
            if filter in ['w', 'weight']:
                weights = kwargs.get('weights',[0,0,0])
            else:
                weights = [1/3,1/3,1/3]
            try:
                wr, wg, wb = weights
                if (wr + wg + wb) == 1.0:
                    for i in range(len(ret)):
                        for j in range(len(ret[i])):
                            if alpha_channel:
                                r, g, b, a = ret[i, j]
                                gray = r * wr + g * wg + b * wb
                                ret[i, j] = (gray, gray, gray, a)
                            else:
                                r, g, b = ret[i, j]
                                gray = r * wr + g * wg + b * wb
                                ret[i, j] = (gray, gray, gray)
                    return ret
                else:
                    return None  
            except Exception:
                return None
            
        return None

