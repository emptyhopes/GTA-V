import os
import ctypes

from Modules.Logger import Print

def Run():
    if AdministratorRights(): return
    else: Exit()

def AdministratorRights():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def Exit():
    Print("Run the script as administrator.")
    exit()