



"""

Example 2


"""


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print (df.dropna(axis=1))



"""

Its output is as follows −

Empty DataFrame
Columns: [ ]
Index: [a, b, c, d, e, f, g, h]

"""

