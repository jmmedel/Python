


"""

Example 4


"""


# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select range of rows for all columns
print (df.loc['a':'h'])


"""

Its output is as follows −

            A           B          C          D
a    0.391548   -0.224297   0.745623   0.054301
b   -0.070649   -0.880130   1.620406   1.419743
c   -0.317212   -1.929698   1.448365   0.616899
d   -2.162406    0.614256  -0.873557   1.093958
e    2.202797   -2.315915   0.528067   0.612482
f    0.613709   -0.157674   0.286414  -0.500517
g    1.050559   -2.272099   0.216526   0.928449
h    1.122680    0.324368  -1.621420  -0.741470


"""


