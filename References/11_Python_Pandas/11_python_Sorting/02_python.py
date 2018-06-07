


"""

By Label
Using the sort_index() method, by passing the axis arguments and the order of sorting, DataFrame can be sorted. By default, sorting is done on row labels in ascending order.


"""

import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
   mns = ['col2','col1'])

sorted_df=unsorted_df.sort_index()
print (sorted_df)


"""

Its output is as follows −

        col2       col1
0   0.208464   0.627037
1   0.641004   0.331352
2  -0.038067  -0.464730
3  -0.638456  -0.021466
4   0.014646  -0.737438
5  -0.290761  -1.669827
6  -0.797303  -0.018737
7   0.525753   1.628921
8  -0.567031   0.775951
9   0.060724  -0.322425


"""
