



"""

Example 2

"""


import pandas as pd
import numpy as np
df = pd.DataFrame({'one':[10,20,30,40,50,2000],
'two':[1000,0,30,40,50,60]})
print (df.replace({1000:10,2000:60}))



"""
Its output is as follows −

   one  two
0   10   10
1   20    0
2   30   30
3   40   40
4   50   50
5   60   60

"""
