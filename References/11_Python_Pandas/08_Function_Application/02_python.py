


"""

Row or Column Wise Function Application
Arbitrary functions can be applied along the axes of a DataFrame or Panel using the apply() method, which, like the descriptive statistics methods, takes an optional axis argument. By default, the operation performs column wise, taking each column as an array-like.

Example 1


"""


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean)
print (df.apply(np.mean))

"""


Its output is as follows −

      col1       col2        col3                                                      
0   0.343569  -1.013287    1.131245 

1   0.508922  -0.949778   -1.600569 

2  -1.182331  -0.420703   -1.725400

3   0.860265   2.069038   -0.537648

4   0.876758  -0.238051    0.473992
By passing axis parameter, operations can be performed row wise.

"""
