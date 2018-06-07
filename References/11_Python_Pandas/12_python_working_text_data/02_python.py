

"""

lower()


"""

import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print (s.str.lower())


"""


Its output is as follows −

0            tom
1   william rick
2           john
3        alber@t
4            NaN
5           1234
6    steve smith
dtype: object


"""

