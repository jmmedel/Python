


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])

for index, row in df.iterrows():
   row['a'] = 10
print (df)

"""

Its output is as follows −

        col1       col2       col3
0  -1.739815   0.735595  -0.295589
1   0.635485   0.106803   1.527922
2  -0.939064   0.547095   0.038585
3  -1.016509  -0.116580  -0.523158



"""
