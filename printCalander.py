import calendar


def YourMonth():

    month = input("\nPlease enter your desired month(1..12): ")

    if int(month) in range(1,12):
        return int(month)
    else:
        return YourMonth()


def YourYear():

    year = input("\nPlease enter your desired year(..2020):")
    print("")

    if len(year) == 4 :
        return int(year)
    else:
        return YourYear()


def YourCalendar():

    month = YourMonth()
    year = YourYear()

    result = calendar.monthcalendar(year,month)
    
    for i in result: 
        print(i)

    terminate = input("\nDo you want to comtinue ([Y]es/[N]o)? ")

    if terminate == "Y":
        YourCalendar()
    elif terminate == "N":
        exit()


YourCalendar()