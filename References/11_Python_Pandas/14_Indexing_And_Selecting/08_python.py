


"""


Example 3


"""


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Slicing through list of values
print (df.iloc[[1, 3, 5], [1, 3]])
print (df.iloc[1:3, :])
print (df.iloc[:,1:3])


"""

Its output is as follows −

           B           D
1   0.890791    0.631615
3  -1.284314   -0.026251
5  -0.512888   -0.518930

           A           B           C           D
1  -0.685354    0.890791   -0.813012    0.631615
2  -0.783192   -0.531378    0.025070    0.230806

           B           C
0   0.256239   -1.270702
1   0.890791   -0.813012
2  -0.531378    0.025070
3  -1.284314    0.826977
4  -0.460729    1.423332
5  -0.512888    0.581409
6  -1.204853    0.098060
7  -0.947857    0.641358

"""
