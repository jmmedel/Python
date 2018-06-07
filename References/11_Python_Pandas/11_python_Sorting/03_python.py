


"""


Order of Sorting
By passing the Boolean value to ascending parameter, the order of the sorting can be controlled. Let us consider the following example to understand the same.


"""


import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
   mns = ['col2','col1'])

sorted_df = unsorted_df.sort_index(ascending=False)
print (sorted_df)


"""

Its output is as follows −

         col2        col1
9    0.825697    0.374463
8   -1.699509    0.510373
7   -0.581378    0.622958
6   -0.202951    0.954300
5   -1.289321   -1.551250
4    1.302561    0.851385
3   -0.157915   -0.388659
2   -1.222295    0.166609
1    0.584890   -0.291048
0    0.668444   -0.061294


"""
