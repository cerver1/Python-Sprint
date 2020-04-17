
# Write a Python program to get a new string from a given string 
# where "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged.

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