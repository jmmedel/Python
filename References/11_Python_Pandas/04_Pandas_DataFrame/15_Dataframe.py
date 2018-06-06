



"""

Selection by integer location
Rows can be selected by passing integer location to an iloc function.



"""


import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df.iloc[2])


"""

Its output is as follows −

one   3.0
two   3.0
Name: c, dtype: float64


"""


