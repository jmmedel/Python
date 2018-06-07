

"""

split(pattern)


"""

import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print s
print ("Split Pattern:")
print (s.str.split(' '))


"""

Its output is as follows −

0            Tom
1   William Rick
2           John
3        Alber@t
dtype: object

Split Pattern:
0   [Tom, , , , , , , , , , ]
1   [, , , , , William, Rick]
2   [John]
3   [Alber@t]
dtype: object


"""

