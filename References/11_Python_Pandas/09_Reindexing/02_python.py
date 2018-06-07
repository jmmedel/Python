



"""


Reindex to Align with Other Objects
You may wish to take an object and reindex its axes to be labeled the same as another object. Consider the following example to understand the same.

Example


"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

df1 = df1.reindex_like(df2)
print (df1)


"""

Its output is as follows −

          col1         col2         col3
0    -2.467652    -1.211687    -0.391761
1    -0.287396     0.522350     0.562512
2    -0.255409    -0.483250     1.866258
3    -1.150467    -0.646493    -0.222462
4     0.152768    -2.056643     1.877233
5    -1.155997     1.528719    -1.343719
6    -1.015606    -1.245936    -0.295275
Note − Here, the df1 DataFrame is altered and reindexed like df2. The column names should be matched or else NAN will be added for the entire column label.


Note − Here, the df1 DataFrame is altered and reindexed like df2. The column names should be matched or else NAN will be added for the entire column label.

"""


