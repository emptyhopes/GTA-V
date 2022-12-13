from datetime import datetime

start = []
end = []
difference = []

def GetTime():
    return datetime.now()

def Start():
    start.append(GetTime())
    print(start[0].strftime("%d.%m.%Y %H:%M:%S.%f") + " - " + "Application started.")
    return start[0]

def End():
    end.append(GetTime())
    print(end[0].strftime("%d.%m.%Y %H:%M:%S.%f") + " - " + "Application ended.")
    return end[0]

def Difference():
    result = end[0] - start[0]
    difference.append(result)
    print(str(difference[0]) + " - " + "Working time.")
    return difference[0]