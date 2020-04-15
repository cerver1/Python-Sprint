# takes string and generates it into a list and tuple

sample = input("Please input a series of numbers: ")

list = sample.split(',')
tuple = tuple(list)

print(list)
print(tuple)