


"""

len()

"""


import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
print (s.str.len())

"""

Its output is as follows −

0    3.0
1   12.0
2    4.0
3    7.0
4    NaN
5    4.0
6   10.0
dtype: float64

"""






