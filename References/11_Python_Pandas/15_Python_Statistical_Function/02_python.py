


"""


Covariance
Covariance is applied on series data. The Series object has a method cov to compute covariance between series objects. NA will be excluded automatically.

Cov Series

"""

import pandas as pd
import numpy as np
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print (s1.cov(s2))


"""

Its output is as follows −

-0.12978405324
Covariance method when applied on a DataFrame, computes cov between all the columns.

"""

