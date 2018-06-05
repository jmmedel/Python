

"""

Create a Series from dict
A dict can be passed as input and if no index is specified, then the dictionary keys are taken in a sorted order to construct index. If index is passed, the values in data corresponding to the labels in the index will be pulled out.

Example 1


"""


#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print (s)


"""

Its output is as follows −

a 0.0
b 1.0
c 2.0
dtype: float64

Observe − Dictionary keys are used to construct index.


"""




