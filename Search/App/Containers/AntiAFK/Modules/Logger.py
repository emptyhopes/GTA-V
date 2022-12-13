from Modules.Time import GetTime

def Print(text):
    print(GetTime().strftime("%d.%m.%Y %H:%M:%S.%f") + " - " + text)
