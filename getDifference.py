

# Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.

given = int(input("Please enter your number: "))

difference = abs(given - 17)

if given > 17:
    print(difference * 2)
else:
    print(difference)
