from json import dump, load

from Modules.Time import Time
from Modules.Logger import Logger
from Modules.Recognition import recognition

from Config.Utils import database_path

class Entry:
    data = None

    date = Time.GetTime().strftime("%d.%m.%Y")
    time = Time.GetTime().strftime("%H:%M:%S.%f")

    def Run ():

        try:
            Entry.Read()
            if (Entry.data[Entry.date]): Entry.Write()
            Logger.Print("Writing from notepad done.")

        except KeyError:
            Entry.data[0][Entry.date] = []

            file = open(database_path, "w")
            dump(Entry.data, file, indent = 5)
            file.close()

            Entry.Write()

            Logger.Print("Writing from notepad done.")


    def Read():
        file = open(database_path, "r")
        Entry.data = load(file)
        file.close()

    def Write():
        Entry.data[Entry.date].append({ "time": Entry.time, "working_time": str(Time.difference), "number": recognition[0] })
        file = open(database_path, "w")
        dump(Entry.data, file, indent = 5)
        file.close()