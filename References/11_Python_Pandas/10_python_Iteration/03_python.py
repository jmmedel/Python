


"""

iterrows()
iterrows() returns the iterator yielding each index value along with a series containing the data in each row.


"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row_index,row in df.iterrows():
   print (row_index,row)


"""

Its output is as follows −

0  col1    1.529759
   col2    0.762811
   col3   -0.634691
Name: 0, dtype: float64

1  col1   -0.944087
   col2    1.420919
   col3   -0.507895
Name: 1, dtype: float64
 
2  col1   -0.077287
   col2   -0.858556
   col3   -0.663385
Name: 2, dtype: float64
3  col1    -1.638578
   col2     0.059866
   col3     0.493482
Name: 3, dtype: float64


Note − Because iterrows() iterate over the rows, it doesn't preserve the data type across the row. 0,1,2 are the row indices and col1,col2,col3 are column indices.

"""

