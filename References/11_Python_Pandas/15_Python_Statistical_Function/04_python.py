


"""

Correlation
Correlation shows the linear relationship between any two array of values (series). There are multiple methods to compute the correlation like pearson(default), spearman and kendall.


"""


import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])

print (frame['a'].corr(frame['b']))

print (frame.corr())


"""

Its output is as follows −

-0.383712785514

           a          b          c          d           e
a   1.000000  -0.383713  -0.145368   0.002235   -0.104405
b  -0.383713   1.000000   0.125311  -0.372821    0.224908
c  -0.145368   0.125311   1.000000  -0.045661   -0.062840
d   0.002235  -0.372821  -0.045661   1.000000   -0.403380
e  -0.104405   0.224908  -0.062840  -0.403380    1.000000

If any non-numeric column is present in the DataFrame, it is excluded automatically.

"""
