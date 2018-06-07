


"""

Example 5


"""


# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# for getting values with a boolean array
print (df.loc['a']>0)

"""

Its output is as follows −

A  False
B  True
C  False
D  False
Name: a, dtype: bool


"""
