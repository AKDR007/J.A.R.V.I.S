import datetime

dt = datetime.datetime

def Current_Time():
    Cur_Time = dt.now().ctime().split()[3][:5]
    return Cur_Time

def Week_Day():
    WD = dt.now().ctime().split()[0]
    return WD

