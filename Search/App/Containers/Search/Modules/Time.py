import datetime

class Time:

    start = None
    end = None
    difference = None

    def __init__ ():
        pass

    def GetTime ():
        return datetime.datetime.now()

    def Start ():
        Time.start = Time.GetTime()
        print(Time.Compare(Time.start) + " - " + "Application started.")

    def End ():
        Time.end = Time.GetTime()
        print(Time.Compare(Time.end) + " - " + "Application ended.")

    def Difference ():
        Time.difference = Time.end - Time.start
        print(Time.Compare(Time.GetTime()) + " - " + "Working time = " + str(Time.difference))

    def Compare (time):
        return time.strftime("%d.%m.%Y %H:%M:%S.%f")