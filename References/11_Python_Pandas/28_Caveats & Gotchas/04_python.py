


"""

Bitwise Boolean
Bitwise Boolean operators like == and != will return a Boolean series, which is almost always what is required anyways.


"""


import pandas as pd

s = pd.Series(range(5))
print (s==4)


"""

Its output is as follows −

0 False
1 False
2 False
3 False
4 True
dtype: bool


"""


