from Modules.Time import Start, End, Difference

import Modules.Administrator
import Modules.Capture
import Modules.AFK

def Run():

    Start()

    Modules.Administrator.Run()
    Modules.Capture.Run()
    Modules.AFK.Run()

    End()

    Difference()