import win32gui
import win32com.client

import time

from Modules.Logger import Logger

class Capture:

    handles = []
    sizes = None

    application = "RAGE Multiplayer"
    success = None

    alphabet_latinic = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabet_cyryllic = ["а", "", "", "", "е", "", "", "", "", "", "", "", "м", "", "", "р", "", "", "", "", "", "", "", "", "у", ""]

    def __init__ ():
        pass

    def Run ():
        win32gui.EnumWindows(Capture.EnumHandler, None)

        Capture.Translation()
        Capture.Comparison()

    def EnumHandler (handle, context):
        if (win32gui.IsWindowVisible(handle) == 0): return
        Capture.handles.append({"name": win32gui.GetWindowText(handle), "source": win32gui.GetWindowText(handle), "translated": "", "handle": handle})

    def Translation ():

        for handle_index, handle in enumerate(Capture.handles):

            handle["source"] = Capture.Formatting(handle["source"])

            # Logger.Print(handle)

            for letter in handle["source"]:

                for index in range(len(Capture.alphabet_latinic)):
                    if (Capture.alphabet_latinic[index] == letter): 
                        Capture.handles[handle_index]["translated"] = Capture.handles[handle_index]["translated"] + Capture.alphabet_latinic[index]
                        # Logger.Print("IT IS A LATINIC", letter)

                for index in range(len(Capture.alphabet_cyryllic)):
                    if (Capture.alphabet_cyryllic[index] == letter): 
                        Capture.handles[handle_index]["translated"] = Capture.handles[handle_index]["translated"] + Capture.alphabet_latinic[index]

    def Comparison ():
        Capture.application = Capture.Formatting(Capture.application)

        for handle in Capture.handles:
            if (handle["translated"] == Capture.application): Capture.success = handle

        if (Capture.success != None): Capture.Success(Capture.success["handle"])
        else: Capture.Exit()

    def Formatting (process):
        return process.lower().replace(" ", "")

    def Success (handle):
        Capture.sizes = win32gui.GetWindowRect(handle)
        Capture.FixSetForegroundWindow()
        win32gui.SetForegroundWindow(handle)
        Logger.Print("RAGE Multiplayer capture done.") 
        time.sleep(1)

    def Exit ():
        Logger.Print("RAGE Multiplayer is not found.")
        time.sleep(1)
        exit()

    def FixSetForegroundWindow ():
        win32com.client.Dispatch("WScript.Shell").SendKeys("%")