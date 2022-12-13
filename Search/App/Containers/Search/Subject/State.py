from Config.Regions import regions
from Config.Utils import image_waiting_path

from Modules.Logger import Logger

from Modules.Capture import Capture
from Modules.Grab import Grab
from Modules.Bleaching import Bleaching
from Modules.Recognition import Recognition

class State:

    text = None

    screen_width = None
    screen_height = None
    offset_screen_width = None
    offset_screen_height = None

    region_waiting_width = None
    region_waiting_height = None
    offset_waiting_width = None
    offset_waiting_height = None

    bbox = None
    box = None

    config = r"-l rus --oem 3 --psm 6"

    def __init__ ():
        pass

    def Run ():

        State.Init()

        image = Grab.Grab(State.bbox)
        image = Grab.Crop(image, State.box)
        
        Grab.Save(image, image_waiting_path)
        # Grab.Resize(image_waiting_path)
        Logger.Print("Grab waiting is done.")

        # Bleaching.Bleach(image_waiting_path)
        # Logger.Print("Bleach waiting is done.")

        # Recognition.Recognite(image_waiting_path, State.config)
        # Logger.Print("Recognite waiting is done.")

        # State.text = Recognition.recognition

    def Init():

        State.screen_width = Capture.sizes[2] - Capture.sizes[0]
        State.screen_height = Capture.sizes[3] - Capture.sizes[1]
        State.offset_screen_width = Capture.sizes[0]
        State.offset_screen_height = Capture.sizes[1]

        for region in regions:
            if (region["width"] == State.screen_width and region["height"] == State.screen_height):
                State.region_waiting_width = region["region_waiting_width"]
                State.region_waiting_height = region["region_waiting_height"]
                State.offset_waiting_width = region["offset_waiting_width"]
                State.offset_waiting_height = region["offset_waiting_height"]
        
        State.bbox = ( State.offset_screen_width, State.offset_screen_height, State.screen_width + State.offset_screen_width, State.screen_height + State.offset_screen_height )
        State.box = ( State.region_waiting_width, State.region_waiting_height, State.screen_width - State.offset_waiting_width, State.screen_height - State.offset_waiting_height )