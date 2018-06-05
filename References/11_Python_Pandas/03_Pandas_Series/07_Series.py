


"""

Accessing Data from Series with Position
Data in the series can be accessed similar to that in an ndarray.

Example 1
Retrieve the first element. As we already know, the counting starts from zero for the array, which means the first element is stored at zeroth position and so on.


"""


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print (s[0])


"""

Its output is as follows −

1


"""
