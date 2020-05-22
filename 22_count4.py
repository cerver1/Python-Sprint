

def find_four():
    
    userList = input("please enter a list of numbers(1,2,3,4): ")

    converted = userList.split(',')
    count = 0

    for i in converted:
        if i == "4" :
            count += 1

    print("\nyour list contains "+str(count)+" number 4\n")

    terminate()


def terminate():

    terminate = input("do you want to end the programm?(Y/N) ").upper()

    if terminate == "Y":
        exit()
    elif terminate == "N":
        find_four()
    else:
        print("\nplease enter either Y or N\n")
        terminate()

find_four()