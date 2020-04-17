

def startsWithIs():

    given = input("Please enter your string: ")

    if given.startswith("Is"):
        print(given)
    else:
        print("Is" + given)

    terminate = input("Do you want to end the program?([Y]es or [N]o) ")

    if terminate == "Y":
        exit()
    elif terminate == "N":
        startsWithIs()


startsWithIs()