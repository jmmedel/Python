


"""


Column Selection
We will understand this by selecting a column from the DataFrame.

Example



"""


import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df ['one'])

"""

Its output is as follows −

a     1.0
b     2.0
c     3.0
d     NaN
Name: one, dtype: float64


"""

