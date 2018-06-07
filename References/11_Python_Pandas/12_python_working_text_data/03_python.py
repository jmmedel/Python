


"""

upper()


"""

import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print (s.str.upper())


"""

Its output is as follows −

0            TOM
1   WILLIAM RICK
2           JOHN
3        ALBER@T
4            NaN
5           1234
6    STEVE SMITH
dtype: object


"""
