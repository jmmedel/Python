


"""


Check for Missing Values
To make detecting missing values easier (and across different array dtypes), Pandas provides the isnull() and notnull() functions, which are also methods on Series and DataFrame objects −

Example 1

"""

import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df['one'].isnull())



"""

Its output is as follows −

a  False
b  True
c  False
d  True
e  False
f  False
g  True
h  False
Name: one, dtype: bool



"""




