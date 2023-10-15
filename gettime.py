import datetime

dt = datetime.datetime


DAY_NAME = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def WeekDay(day):
    match day:
        case 0:
            print(("\n{}\n").format(DAY_NAME[0]))
        case 1:
            print(("\n{}\n").format(DAY_NAME[1]))
        case 2:
            print(("\n{}\n").format(DAY_NAME[2]))
        case 3:
            print(("\n{}\n").format(DAY_NAME[3]))
        case 4:
            print(("\n{}\n").format(DAY_NAME[4]))
        case 5:
            print(("\n{}\n").format(DAY_NAME[5]))
        case 6:
            print(("\n{}\n").format(DAY_NAME[6]))
        case default:
            print("\nError\n")

day = dt.now().weekday()
WeekDay(day)

