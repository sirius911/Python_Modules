import numpy as np
from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor

spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))

imp = ImageProcessor()
arr = imp.load("../resources/42AI.png")
new_arr = spb.crop(arr, (100,80), (50,50))
print(new_arr.shape)
imp.display(new_arr)
new_arr= spb.crop(arr, (1000,1000), (1000,1000))
print(new_arr)

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
arr2_thin = spb.thin(arr2,3,0)
print(arr2_thin, end="")
print(type(arr2_thin))

imp.display(spb.thin(arr, 2, 0))


arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
arr3_jux = spb.juxtapose(arr3, 3, 1)
print(arr3_jux,end="")
print(type(arr3_jux))
spb.juxtapose("arr", 4, 2) # return None
spb.juxtapose(arr, -42, 2) # return None
spb.juxtapose(arr, 4, 2) # return None

imp.display(spb.juxtapose(arr, 3 ,1))

imp.display(spb.juxtapose(arr, 4, 0))

imp.display(spb.mosaic(arr, (4, 3)))