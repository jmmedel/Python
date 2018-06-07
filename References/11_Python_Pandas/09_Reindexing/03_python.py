



"""


Filling while ReIndexing
reindex() takes an optional parameter method which is a filling method with values as follows −

pad/ffill − Fill values forward

bfill/backfill − Fill values backward

nearest − Fill from the nearest index values

Example



"""


import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print (df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill:")
print (df2.reindex_like(df1,method='ffill'))


"""

Its output is as follows −

         col1        col2       col3
0    1.311620   -0.707176   0.599863
1   -0.423455   -0.700265   1.133371
2         NaN         NaN        NaN
3         NaN         NaN        NaN
4         NaN         NaN        NaN
5         NaN         NaN        NaN

Data Frame with Forward Fill:
         col1        col2        col3
0    1.311620   -0.707176    0.599863
1   -0.423455   -0.700265    1.133371
2   -0.423455   -0.700265    1.133371
3   -0.423455   -0.700265    1.133371
4   -0.423455   -0.700265    1.133371
5   -0.423455   -0.700265    1.133371
Note − The last four rows are padded.


"""
