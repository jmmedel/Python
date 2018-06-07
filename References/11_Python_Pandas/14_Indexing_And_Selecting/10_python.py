


"""

Example 2


"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
# Index slicing
print (df.ix[:,'A'])


"""

Its output is as follows −

0   0.699435
1  -0.685354
2  -0.783192
3   0.539042
4  -1.044209
5  -1.415411
6   1.062095
7   0.994204
Name: A, dtype: float64


"""
