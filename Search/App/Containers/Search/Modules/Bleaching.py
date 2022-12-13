import cv2

class Bleaching:
    thresh = 160

    def __init__ ():
        pass

    def Bleach (path):
        image = cv2.imread(path)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_binary = cv2.threshold(image_gray, Bleaching.thresh, 255, 0)[1]

        cv2.imwrite(path, image_binary)