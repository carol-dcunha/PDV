from pandas import DataFrame
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

frame=DataFrame(data,index=labels,columns=["animal","age","visits","priority"])
print frame
print "Information\n"
print frame.info()
print "Description\n"
print frame.describe()

print "\nFirst 3 rows:"
print frame.ix[:3]

print "\nAnimal and Age columns:"
print frame[['animal','age']]

print "data in rows [3, 4, 8] and in columns ['animal', 'age']"
print frame[[3,4,8],['animal', 'age']]