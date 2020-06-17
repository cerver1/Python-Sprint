import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

labels = ['a', 'b', 'c']
myList = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10, 'b': 20, 'c':100}

ser1 = pd.Series([1,2,3,4], index = ['USA', 'CHINA', 'FRANCE', 'GERMANY'])

ser2 = pd.Series([1,2,3,4], index = ['USA', 'CHINA', 'ITALY', 'JAPAN'])

# you can pull data based on its index
ser1['USA']

# you can also add matching data
ser1 + ser2


# DATA FRAMES I

# df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

# df['W'] does the same thing as df.W but df['W'] is safer to use 

# to call multiple methods
# df[['W','Z']]
'''
df['new'] = df['W'] + df['Y']

df.drop('new', axis = 1, inplace = True) # inplace = True is required for permanent changes
df.loc['A'] # row name based index 
df.iloc[2] # numeric based index as found on regular lists
df.loc[['A','B'],['W','Y']] # getting specific rows and columns
'''

# DATA FRAMES III

outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])

# df.loc['G1'].loc[1]

# df.index.names = ["Groups", 'Num']  to name specific columns

# df.loc['G2'].loc[2]['B'] grabbing nested data
# df.xs(1, level= 'Num') to grab a specific crossection of data at a row and column




print()