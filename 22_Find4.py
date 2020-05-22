

def count_four():
    
    userList = input("please enter a list of numbers(1,2,3,4): ")

    converted = userList.split(',')

    if len(converted) >= 4:
        print("\nyour list is greater than 4 items \n")
        print(converted)
    else:
        print("\nyour list is less than 4 items \n")
        print(converted)
    
    terminate = input("Do you want to end the programm?(Y/N) ")
    if terminate == "Y":
        exit()
    elif terminate == "N":
        count_four()



count_four()