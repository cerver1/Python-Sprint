
# Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return three times of their sum.


def triSum():

    num_1 = int(input("Please enter your first number: "))

    num_2 = int(input("Please enter your second number: "))

    num_3 = int(input("Please enter your third number: "))

    sum = num_1 + num_2 + num_3

    if num_1 == num_2 and num_1 == num_3:
        print(sum * 3)
    else:
        print(sum)

    terminate = input("Do you want to end the program?([Y]es or [N]o) ")

    if terminate == "Y":
        exit()
    elif terminate == "N":
        triSum()


triSum()