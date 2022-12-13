from Modules.Time import Time

from Modules.Rights import Rights
from Modules.Capture import Capture

from Subject.Number import Number
from Subject.State import State

from Modules.Tests import Tests

def Run():

    Time.Start()

    Tests.Run()

    # Rights.Run()
    # Capture.Run()

    # Number.Run()
    # State.Run()

    # while (True):
        # Number.Run()
        # print(Number.number.replace(" ", ""))

        # State.Run()
        # print(Waiting.text.replace(" ", ""))
        
        # time.sleep(0.5)


    Time.End()

    Time.Difference()