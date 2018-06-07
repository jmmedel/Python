


"""

.ix()
Besides pure label based and integer based, Pandas provides a hybrid method for selections and subsetting the object using the .ix() operator.

Example 1


"""



import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Integer slicing
print (df.ix[:4])


"""

Its output is as follows −

           A          B           C           D
0   0.699435   0.256239   -1.270702   -0.645195
1  -0.685354   0.890791   -0.813012    0.631615
2  -0.783192  -0.531378    0.025070    0.230806
3   0.539042  -1.284314    0.826977   -0.026251


"""


