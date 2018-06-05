

"""

Example 2
Retrieve the first three elements in the Series. If a : is inserted in front of it, all items from that index onwards will be extracted. If two parameters (with : between them) is used, items between the two indexes (not including the stop index)


"""

import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first three element
print (s[:3])


"""

Its output is as follows −

a  1
b  2
c  3
dtype: int64


"""
