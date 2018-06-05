



"""

Example 2
Retrieve multiple elements using a list of index label values.


"""

import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve multiple elements
print s[['a','c','d']]


"""

Its output is as follows −

a  1
c  3
d  4
dtype: int64


"""

