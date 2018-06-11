



"""

sin Operation
This returns a Boolean series showing whether each element in the Series is exactly contained in the passed sequence of values.


"""


import pandas as pd

s = pd.Series(list('abc'))
s = s.isin(['a', 'c', 'e'])
print (s)


"""

Its output is as follows −

0 True
1 False
2 True
dtype: bool


"""


