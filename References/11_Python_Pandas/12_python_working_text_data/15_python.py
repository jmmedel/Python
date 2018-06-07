


"""

find(pattern)


"""


import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.find('e'))

"""

Its output is as follows −

0  -1
1  -1
2  -1
3   3
dtype: int64

"-1" indicates that there no such pattern available in the element.

"""