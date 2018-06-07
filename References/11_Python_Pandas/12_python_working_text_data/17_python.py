


"""

swapcase()

"""


import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print (s.str.swapcase())


"""
Its output is as follows −

0  tOM
1  wILLIAM rICK
2  jOHN
3  aLBER@T
dtype: object

"""

