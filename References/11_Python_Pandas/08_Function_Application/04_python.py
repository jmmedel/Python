


"""


Element Wise Function Application
Not all functions can be vectorized (neither the NumPy arrays which return another array nor any value), the methods applymap() on DataFrame and analogously map() on Series accept any Python function taking a single value and returning a single value.

Example 1


"""


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])

# My custom function
df['col1'].map(lambda x:x*100)
print (df.apply(np.mean))


"""

Its output is as follows −

       col1      col2       col3    
		
0    0.629348  0.088467  -1.790702 
                                               
1   -0.592595  0.184113  -1.524998

2   -0.419298  0.262369  -0.178849

3   -1.036930  1.103169   0.941882 

4   -0.573333 -0.031056   0.315590


"""

