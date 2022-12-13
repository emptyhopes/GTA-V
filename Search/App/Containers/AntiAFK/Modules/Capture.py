from win32gui import EnumWindows, IsWindowVisible, GetWindowText, SetForegroundWindow, GetWindowRect
from win32com.client import Dispatch

from time import sleep

from Modules.Logger import Print

handles = []
sizes = []

def Run():
    EnumWindows(EnumHandler, None)
    Translation()
    Comparison()

def EnumHandler(handle, context):
    if (IsWindowVisible(handle) == 0): return
    handles.append({"name": GetWindowText(handle), "source": GetWindowText(handle), "translated": "", "handle": handle})

def Translation():

    alphabet_latinic = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabet_cyryllic = ["а", "", "", "", "е", "", "", "", "", "", "", "", "м", "", "", "р", "", "", "", "", "", "", "", "", "у", ""]

    for handle_index, handle in enumerate(handles):

        handle["source"] = Formatting(handle["source"])

        # Print(handle)

        for letter in handle["source"]:

            for index in range(len(alphabet_latinic)):
                if (alphabet_latinic[index] == letter): 
                    handles[handle_index]["translated"] = handles[handle_index]["translated"] + alphabet_latinic[index]
                    # Print("IT IS A LATINIC", letter)

            for index in range(len(alphabet_cyryllic)):
                if (alphabet_cyryllic[index] == letter): 
                    handles[handle_index]["translated"] = handles[handle_index]["translated"] + alphabet_latinic[index]

def Comparison():

    success = []

    application = "RAGE Multiplayer"
    application = Formatting(application)

    for handle in handles:
        if (handle["translated"] == application): success.append(handle)

    if (len(success) > 0): Success(success[0]["handle"])
    else: Exit()

def Formatting(process):
    return process.lower().replace(" ", "")

def Success(handle):
    FixSetForegroundWindow()
    SetForegroundWindow(handle)
    sizes.append(GetWindowRect(handle))
    Print("RAGE Multiplayer capture done.") 
    sleep(1)

def FixSetForegroundWindow():
    Dispatch("WScript.Shell").SendKeys("%")

def Exit():
    Print("RAGE Multiplayer is not found.")
    exit()