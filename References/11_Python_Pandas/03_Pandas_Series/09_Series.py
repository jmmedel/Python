

"""

Example 3
Retrieve the last three elements.



"""


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the last three element
print (s[-3:])


"""

Its output is as follows −

c  3
d  4
e  5
dtype: int64


"""
