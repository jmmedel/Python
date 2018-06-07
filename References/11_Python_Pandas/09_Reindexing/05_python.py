



"""


Renaming
The rename() method allows you to relabel an axis based on some mapping (a dict or Series) or an arbitrary function.

Let us consider the following example to understand this −

"""


import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print (df1)

print ("After renaming the rows and columns:")
print (df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))



"""

Its output is as follows −

         col1        col2        col3
0    0.486791    0.105759    1.540122
1   -0.990237    1.007885   -0.217896
2   -0.483855   -1.645027   -1.194113
3   -0.122316    0.566277   -0.366028
4   -0.231524   -0.721172   -0.112007
5    0.438810    0.000225    0.435479

After renaming the rows and columns:
                c1          c2        col3
apple     0.486791    0.105759    1.540122
banana   -0.990237    1.007885   -0.217896
durian   -0.483855   -1.645027   -1.194113
3        -0.122316    0.566277   -0.366028
4        -0.231524   -0.721172   -0.112007
5         0.438810    0.000225    0.435479
The rename() method provides an inplace named parameter, which by default is False and copies the underlying data. Pass inplace=True to rename the data in place.


"""
