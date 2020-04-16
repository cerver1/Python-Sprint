# Program to get the documents around a builtin function


sample = input("Please enter a builtin function: ")

print(help(sample))

print(eval(input('Enter a built in function: ')).__doc__)