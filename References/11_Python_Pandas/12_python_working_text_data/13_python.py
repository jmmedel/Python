


"""

startswith(pattern)


"""


import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print ("Strings that start with 'T':")
print (s.str. startswith ('T'))

"""

Its output is as follows −

0  True
1  False
2  False
3  False
dtype: bool


"""

