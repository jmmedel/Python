


"""

Use of Notations
Getting values from the Pandas object with Multi-axes indexing uses the following notation −

Object	Indexers	Return Type
Series	s.loc[indexer]	Scalar value
DataFrame	df.loc[row_index,col_index]	Series object
Panel	p.loc[item_index,major_index, minor_index]	p.loc[item_index,major_index, minor_index]
Note − .iloc() & .ix() applies the same indexing options and Return value.

Let us now see how each operation can be performed on the DataFrame object. We will use the basic indexing operator '[ ]' −

Example 1


"""


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print (df['A'])


"""

Its output is as follows −

0  -0.478893
1   0.391931
2   0.336825
3  -1.055102
4  -0.165218
5  -0.328641
6   0.567721
7  -0.759399
Name: A, dtype: float64

"""