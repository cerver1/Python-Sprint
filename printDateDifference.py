import re

def firstDate():

    date = input("Please enter your first date (00/00/0000): ")
    
    datePattern = r"^\d{1,2}\/\d{1,2}\/\d{4}$"

    if re.search(datePattern,date):
        return date.split("/")
    else: 
        print("\nInvalid")
        return firstDate()

def secondDate():

    date = input("Please enter your second date (00/00/0000): ")
    
    datePattern = r"^\d{1,2}\/\d{1,2}\/\d{4}$"

    if re.search(datePattern,date):
        return date.split("/")
    else: 
        print("\nInvalid")
        return secondDate()

def dateDifference():

    first_date = firstDate()
    second_date = secondDate()

    day = int(first_date[1]) - int(second_date[1])
    month = int(first_date[0]) - int(second_date[0])
    year = int(first_date[2]) - int(second_date[2])

    print("Your dates are {} Month, {} Day, {} Year apart".format(abs(month),abs(day),abs(year)))


dateDifference()