


"""

Apply Different Functions to Different Columns of a Dataframe


"""


import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randn(3, 4),
      index = pd.date_range('1/1/2000', periods=3),
      columns = ['A', 'B', 'C', 'D'])
print (df)

r = df.rolling(window=3,min_periods=1)
print (r.aggregate({'A' : np.sum,'B' : np.mean}))



"""

Its output is as follows −

                    A          B          C         D
2000-01-01  -1.575749  -1.018105   0.317797  0.545081
2000-01-02  -0.164917  -1.361068   0.258240  1.113091
2000-01-03   1.258111   1.037941  -0.047487  0.867371
                    A          B
2000-01-01  -1.575749  -1.018105
2000-01-02  -1.740666  -1.189587
2000-01-03  -0.482555  -0.447078


"""

