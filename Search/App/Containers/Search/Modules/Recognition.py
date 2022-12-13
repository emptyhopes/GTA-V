import pytesseract

from Config.Utils import tesseract_path

from PIL import Image 

class Recognition:

    recognition = None

    def __init__ ():
        pass

    def Recognite (path, config):

        Recognition.Clear()
        Recognition.Init()

        image = Image.open(path)

        Recognition.recognition = pytesseract.image_to_string(image, config = config)
        
    def Clear ():
        Recognition.recognition = None

    def Init():
        pytesseract.pytesseract.tesseract_cmd = tesseract_path