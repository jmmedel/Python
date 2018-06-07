


"""


iteritems()
Iterates over each column as key, value pair with label as key and column value as a Series object.



"""


import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   (print key,value)


"""

Its output is as follows −

col1 0    0.802390
1    0.324060
2    0.256811
3    0.839186
Name: col1, dtype: float64

col2 0    1.624313
1   -1.033582
2    1.796663
3    1.856277
Name: col2, dtype: float64

col3 0   -0.022142
1   -0.230820
2    1.160691
3   -0.830279
Name: col3, dtype: float64

Observe, each column is iterated separately as a key-value pair in a Series.

"""

