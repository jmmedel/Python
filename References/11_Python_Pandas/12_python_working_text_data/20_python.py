


"""

isnumeric()

"""


import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])

print (s.str.isnumeric())



"""
Its output is as follows −

0  False
1  False
2  False
3  False
dtype: bool

"""
