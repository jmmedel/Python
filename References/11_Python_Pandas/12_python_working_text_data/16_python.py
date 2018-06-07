


"""

findall(pattern)


"""


import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.findall('e'))


"""

Its output is as follows −

0 []
1 []
2 []
3 [e]
dtype: object
Null list([ ]) indicates that there is no such pattern available in the element.


"""