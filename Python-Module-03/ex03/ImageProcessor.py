import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

class ImageProcessor:
    """Class to load and display images to upcommig exercices"""

    def __init__(self) -> None:
        pass

    def load(self, path, show = False):
        """opens the PNG file specified by the path argument and returns an
        array with the RGB values of the pixels image. 
        Display a message specifying the dimensions of the image"""
        try:
            self.img = mpimg.imread(path)
            print(self.img.shape)
            x = self.img.shape[0]
            y = self.img.shape[1]
            print(f"Loading image of dimensions {x} x {y}")
            plt.imshow(self.img)

            # if self.img.dtype == np.float32:   # to cast in int
                # self.img = (self.img * 255).astype(np.uint8)
            if show:
                plt.title(path)
                plt.show()

        except FileNotFoundError as e:
            print("Exception: FileNotFoundError -- strerror:",e.strerror)
            return None
        except OSError as e:
            print("Exception: OSError -- strerror:",e.strerror)
            return None
        return self.img

    def display(self, array, title=""):
        """takes a numpy array as an argument and displays the corre-
            sponding RGB image.
        """
        try:
            plt.imshow(array)
            plt.title(title)
            plt.show()
        except Exception as e:
            print("Exception: bad array")