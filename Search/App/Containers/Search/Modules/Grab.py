import cv2

from PIL import ImageGrab

class Grab:

    def __init__ ():
        pass

    def Grab (bbox):
        image = ImageGrab.grab(bbox)
        return image

    def Crop (image, box):
        image = image.crop(box)
        return image

    def Save (image, path):
        image.save(path)
    
    def Resize (path):
        image = cv2.imread(path)
        image = cv2.resize(image, None, fx=10, fy=10)
        cv2.imwrite(path, image)