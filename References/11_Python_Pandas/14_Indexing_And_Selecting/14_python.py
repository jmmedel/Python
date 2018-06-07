


"""

Attribute Access
Columns can be selected using the attribute operator '.'.

Example


"""


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

print (df.A)


"""
Its output is as follows −

0   -0.478893
1    0.391931
2    0.336825
3   -1.055102
4   -0.165218
5   -0.328641
6    0.567721
7   -0.759399
Name: A, dtype: float64
"""
