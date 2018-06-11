


"""


Any sparse object can be converted back to the standard dense form by calling to_dense −


"""

import pandas as pd
import numpy as np
ts = pd.Series(np.random.randn(10))
ts[2:-2] = np.nan
sts = ts.to_sparse()
print (sts.to_dense())

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

"""

