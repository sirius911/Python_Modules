import sys
from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter

files = ["elon_canaGAN.png","42AI.png","ours.png"]
path = "../resources/"

if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        if num < 0 or num >= len(files):
            num = 1
        path_image = path + files[num]
    except Exception as e:
        print(e)
        path_image = path + str(sys.argv[1])
else:
    path_image = path + files[1] 

imp = ImageProcessor()
arr = imp.load(path_image)
if arr is None:
    quit()
cf = ColorFilter()
imp.display(arr, "Original image")
imp.display(cf.invert(arr), "Invert Filter")
imp.display(cf.to_blue(arr), "BLue Filter")
imp.display(cf.to_green(arr), "Green Filter")
imp.display(cf.to_red(arr), "Red Filter")

imp.display(cf.to_grayscale(arr, 'weight', weights = [0.2, 0.3, 0.5],alpha=True), "Gray Scale with weights")
imp.display(cf.to_grayscale(arr, 'm'), "Gray Scale with mean")
imp.display(cf.to_grayscale(arr, 'm', alpha=False), "Gray Scale with mean without alpha")
imp.display(cf.to_celluloid(arr), "Celluloid Filter")
imp.display(arr, "Original image")