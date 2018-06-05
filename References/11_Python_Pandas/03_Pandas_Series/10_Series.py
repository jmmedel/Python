



"""

Retrieve Data Using Label (Index)
A Series is like a fixed-size dict in that you can get and set values by index label.

Example 1
Retrieve a single element using index label value.


"""


import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve a single element
print (s['a'])

"""

Its output is as follows −

1


"""


