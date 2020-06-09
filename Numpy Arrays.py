import numpy as np

my_list = [1, 2, 3]

np.array(my_list)

my_matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

np.array(my_matrix)

x = np.zeros((5, 5))

o = np.linspace(0, 10, 30)

eye = np.eye(4)

r = np.random.rand(5, 4)

rn = np.random.randn(5, 4)

r_int = np.random.randint(1, 100, 10)
# print(r_int)

arr = np.arange(25)
ranarr = np.random.randint(0, 50, 10)

# print(arr.reshape(5,5))
# arg allows you to get the index of the value max or min
# print(ranarr.argmax())
arr + 100
arr + arr

arr = np.arange(1, 11)

# you need the code below to explicitly copy your array or all edits happen permanently
arr_copy = arr.copy()

# grabs a specific row
my_matrix[1]

my_matrix[:2, 1:]

# indexing out specific grids in your matrix / list of lists
# :2 means grab everything at the start up until 2 | 1: means starting at 1 grab till the end
my_matrix[:2, 1:]

# CONDITIONAL SELECTION
# example
bool_arr = arr > 4
arr[bool_arr]
# below is produces the same result as the above
arr[arr > 4]
print()
