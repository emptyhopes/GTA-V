from Config.Utils import tests, tesseract_path

import cv2
import pytesseract

from PIL import Image 

class Tests:

    number_thresh = 159
    state_thresh = 159

    number_config = r"--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789"
    state_config = r"--psm 11 --oem 3"

    all = 0
    hit = 0
    failed = 0

    def __init__ ():
        pass

    def Run ():

        Tests.all = 0
        Tests.hit = 0
        Tests.failed = 0

        if (Tests.number_thresh == 255):
            print(Tests.result)
            exit()

        pytesseract.pytesseract.tesseract_cmd = tesseract_path

        for object in tests:

            if (object["subject"] == "number"):
                Tests.Test(object, Tests.number_thresh, "eng", Tests.number_config)

            if (object["subject"] == "state"):
                Tests.Test(object, Tests.state_thresh, "rus", Tests.state_config)

        print("ALL = " + str(Tests.all))
        print("HIT = " + str(Tests.hit))
        print("FAILED = " + str(Tests.failed))

    def Test (object, thresh, lang, config):
        image = cv2.imread(object["path"])
        image = cv2.resize(image, None, fx=5, fy=5)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.threshold(image, thresh, 255, 0)[1]
        image = cv2.medianBlur(image,5)
        cv2.imwrite(object["save"], image)

        recognition = pytesseract.image_to_string(Image.open(object["save"]), lang = lang, config = config).strip().replace("\n", "").replace("\n", "\f").replace(" ", "")

        Tests.all = Tests.all + 1

        if (recognition == object["text"]):
            print("УСПЕХ", recognition)
            Tests.hit = Tests.hit + 1
        else:
            print("FAILED", recognition)
            Tests.failed = Tests.failed + 1

        return recognition