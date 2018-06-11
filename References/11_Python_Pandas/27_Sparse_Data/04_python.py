


"""


Sparse Dtypes
Sparse data should have the same dtype as its dense representation. Currently, float64, int64 and booldtypes are supported. Depending on the original dtype, fill_value default changes −

float64 − np.nan

int64 − 0

bool − False

Let us execute the following code to understand the same 


"""


import pandas as pd
import numpy as np

s = pd.Series([1, np.nan, np.nan])
print (s)

s.to_sparse()
print (s)


"""

Its output is as follows −

0   1.0
1   NaN
2   NaN
dtype: float64

0   1.0
1   NaN
2   NaN
dtype: float64

"""