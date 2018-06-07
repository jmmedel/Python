


"""

Python Pandas - Statistical Functions

Statistical methods help in the understanding and analyzing the behavior of data. We will now learn a few statistical functions, which we can apply on Pandas objects.

Percent_change
Series, DatFrames and Panel, all have the function pct_change(). This function compares every element with its prior element and computes the change percentage.

"""


import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,4])
print (s.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print (df.pct_change())


"""

Its output is as follows −

0        NaN
1   1.000000
2   0.500000
3   0.333333
4   0.250000
5  -0.200000
dtype: float64

            0          1
0         NaN        NaN
1  -15.151902   0.174730
2  -0.746374   -1.449088
3  -3.582229   -3.165836
4   15.601150  -1.860434
By default, the pct_change() operates on columns; if you want to apply the same row wise, then use axis=1() argument.


"""
