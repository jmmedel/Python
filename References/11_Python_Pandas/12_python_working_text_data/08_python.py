


"""

get_dummies()


"""

import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print s.str.get_dummies()


"""

Its output is as follows −

   William Rick   Alber@t   John   Tom
0             0         0      0     1
1             1         0      0     0
2             0         0      1     0
3             0         1      0     0

"""
