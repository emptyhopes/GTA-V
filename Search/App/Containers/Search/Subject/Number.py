from Config.Regions import regions
from Config.Utils import image_number_path

from Modules.Logger import Logger

from Modules.Capture import Capture
from Modules.Grab import Grab
from Modules.Bleaching import Bleaching
from Modules.Recognition import Recognition

class Number:

    number = None

    screen_width = None
    screen_height = None
    offset_screen_width = None
    offset_screen_height = None

    region_number_width = None
    region_number_height = None
    offset_number_width = None
    offset_number_height = None

    bbox = None
    box = None

    config = r"--oem 3 --psm 7"

    def __init__ ():
        pass

    def Run ():

        Number.Init()

        image = Grab.Grab(Number.bbox)
        image = Grab.Crop(image, Number.box)

        Grab.Save(image, image_number_path)
        # Grab.Resize(image_number_path)
        Logger.Print("Grab number is done.")

        # Bleaching.Bleach(image_number_path)
        # Logger.Print("Bleach number is done.")

        # Recognition.Recognite(image_number_path, Number.config)
        # Logger.Print("Recognite number is done.")

        # Number.number = Recognition.recognition

    def Init():

        Number.screen_width = Capture.sizes[2] - Capture.sizes[0]
        Number.screen_height = Capture.sizes[3] - Capture.sizes[1]
        Number.offset_screen_width = Capture.sizes[0]
        Number.offset_screen_height = Capture.sizes[1]

        for region in regions:
            if (region["width"] == Number.screen_width and region["height"] == Number.screen_height):
                Number.region_number_width = region["region_number_width"]
                Number.region_number_height = region["region_number_height"]
                Number.offset_number_width = region["offset_number_width"]
                Number.offset_number_height = region["offset_number_height"]
        
        Number.bbox = ( Number.offset_screen_width, Number.offset_screen_height, Number.screen_width + Number.offset_screen_width, Number.screen_height + Number.offset_screen_height )
        Number.box = ( Number.region_number_width, Number.region_number_height, Number.screen_width - Number.offset_number_width, Number.screen_height - Number.offset_number_height )