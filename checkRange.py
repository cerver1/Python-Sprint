
# Write a Python program to test whether a number is 
# within 100 of 1000 or 2000.

given = int(input("Please enter your number: "))

def withinRange(int):
    return ((abs(1000 - int) <= 100) | (abs(2000 - int) <= 100))

print(withinRange(given))