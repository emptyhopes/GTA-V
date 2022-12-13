import os
import ctypes

from Modules.Logger import Logger

class Rights ():

    def __init__ ():
        pass

    def Run ():
        if Rights.AdministratorRights(): return
        else: Rights.Exit()

    def AdministratorRights ():
        try:
            return os.getuid() == 0
        except AttributeError:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0

    def Exit ():
        Logger.Print("Run the script as administrator.")
        exit()