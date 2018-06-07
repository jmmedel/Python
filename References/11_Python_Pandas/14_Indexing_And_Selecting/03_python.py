


"""

Example 3

"""

# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select few rows for multiple columns, say list[]
print (df.loc[['a','b','f','h'],['A','C']])


"""

Its output is as follows −

           A          C
a   0.391548   0.745623
b  -0.070649   1.620406
f   0.613709   0.286414
h   1.122680  -1.621420


"""

