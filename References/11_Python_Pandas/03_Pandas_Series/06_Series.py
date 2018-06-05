


"""

Create a Series from Scalar
If data is a scalar value, an index must be provided. The value will be repeated to match the length of index


"""

#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
s = pd.Series(5, index=[0, 1, 2, 3])
print (s)


"""

Its output is as follows −

0  5
1  5
2  5
3  5
dtype: int64


"""


