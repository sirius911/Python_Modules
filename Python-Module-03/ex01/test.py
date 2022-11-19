from ImageProcessor import ImageProcessor
import numpy as np

imp = ImageProcessor()
arr = imp.load("non_existing_file.png")
arr = imp.load("../resources/empty.png")
print (arr)
arr = imp.load("../resources/42AI.png")
imp.display(arr)

arr=np.identity(200)
imp.display(arr)

arr=np.random.rand(200,150)
imp.display(arr)

imp.display("Toto")