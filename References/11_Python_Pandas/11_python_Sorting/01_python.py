


"""
Python Pandas - Sorting

There are two kinds of sorting available in Pandas. They are −

By label
By Actual Value
Let us consider an example with an output.


"""


import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
mns=['col2','col1'])
print unsorted_df



"""

Its output is as follows −

        col2       col1
1  -2.063177   0.537527
4   0.142932  -0.684884
6   0.012667  -0.389340
2  -0.548797   1.848743
3  -1.044160   0.837381
5   0.385605   1.300185
9   1.031425  -1.002967
8  -0.407374  -0.435142
0   2.237453  -1.067139
7  -1.445831  -1.701035
In unsorted_df, the labels and the values are unsorted. Let us see how these can be sorted.


"""


