import errno
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os

class ImageProcessor:
    """Class to load and display images to upcommig exercices"""

    def __init__(self) -> None:
        pass

    def load(self, path):
        """opens the PNG file specified by the path argument and returns an
        array with the RGB values of the pixels image. 
        Display a message specifying the dimensions of the image"""
        try:
            self.img = mpimg.imread(path)
            x = self.img.shape[0]
            y = self.img.shape[1]
            print(f"Loading image of dimensions {x} x {y}")
            plt.imshow(self.img)
            plt.show()

        except FileNotFoundError as e:
            print("Exception: FileNotFoundError -- strerror:",e.strerror)
            return None
        except OSError as e:
            print("Exception: OSError -- strerror:",e.strerror)
            return None
        return self.img

    def display(self, array):
        """takes a numpy array as an argument and displays the corre-
            sponding RGB image.
        """
        try:
            plt.imshow(array)
            plt.show()
        except Exception as e:
            print("Exception: bad array")