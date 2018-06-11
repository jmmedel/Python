


"""

Python Pandas - Sparse Data


Sparse objects are “compressed” when any data matching a specific value (NaN / missing value, though any value can be chosen) is omitted. A special SparseIndex object tracks where data has been “sparsified”. This will make much more sense in an example. All of the standard Pandas data structures apply the to_sparse method −

"""


import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(10))
ts[2:-2] = np.nan
sts = ts.to_sparse()
print (sts)

"""

Its output is as follows −

0   -0.810497
1   -1.419954
2         NaN
3         NaN
4         NaN
5         NaN
6         NaN
7         NaN
8    0.439240
9   -1.095910
dtype: float64
BlockIndex
Block locations: array([0, 8], dtype=int32)
Block lengths: array([2, 2], dtype=int32)


"""
