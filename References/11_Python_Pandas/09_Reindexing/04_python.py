



"""

Limits on Filling while Reindexing
The limit argument provides additional control over filling while reindexing. Limit specifies the maximum count of consecutive matches. Let us consider the following example to understand the same −

Example



"""


import pandas as pd
import numpy as np
 
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print (df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill limiting to 1:")
print (df2.reindex_like(df1,method='ffill',limit=1))

"""

Its output is as follows −

         col1        col2        col3
0    0.247784    2.128727    0.702576
1   -0.055713   -0.021732   -0.174577
2         NaN         NaN         NaN
3         NaN         NaN         NaN
4         NaN         NaN         NaN
5         NaN         NaN         NaN

Data Frame with Forward Fill limiting to 1:
         col1        col2        col3
0    0.247784    2.128727    0.702576
1   -0.055713   -0.021732   -0.174577
2   -0.055713   -0.021732   -0.174577
3         NaN         NaN         NaN
4         NaN         NaN         NaN
5         NaN         NaN         NaN

Note − Observe, only the 7th row is filled by the preceding 6th row. Then, the rows are left as they are.


"""
