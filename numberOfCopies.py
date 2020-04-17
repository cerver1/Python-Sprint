
# Write a Python program to get a string which is n (non-negative integer) 
# copies of a given string.

def copies():

    to_copy = input("Please enter your string: ")
    copy_number = int(input("Please enter the amount of copies: "))

    result = ""
    loop = 0

    while loop < copy_number:
        result = result + to_copy
        loop += 1

    print(result)

    terminate = input("Do you want to end the program?([Y]es or [N]o) ")

    if terminate == "Y":
        exit()
    elif terminate == "N":
        copies()


copies()