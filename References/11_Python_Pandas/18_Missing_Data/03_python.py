


"""

Example 2

"""


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df['one'].notnull())


"""


Its output is as follows −

a  True
b  False
c  True
d  False
e  True
f  True
g  False
h  True
Name: one, dtype: bool

Calculations with Missing Data
When summing data, NA will be treated as Zero
If the data are all NA, then the result will be NA

"""

