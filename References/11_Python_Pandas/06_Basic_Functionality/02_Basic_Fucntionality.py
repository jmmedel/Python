

"""

axes
Returns the list of the labels of the series.


"""


import pandas as  pd
import numpy as np 

#Create a series with 4 random numbers

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print (s)

print ("The actual data series is:")
print (s.values)

"""

Its output is as follows −

0   1.787373
1  -0.605159
2   0.180477
3  -0.140922
dtype: float64

The actual data series is:
[ 1.78737302 -0.60515881 0.18047664 -0.1409218 ]


"""

