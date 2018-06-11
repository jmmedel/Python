


"""

The sparse objects exist for memory efficiency reasons.

Let us now assume you had a large NA DataFrame and execute the following code −



"""


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10000, 4))
df.ix[:9998] = np.nan
sdf = df.to_sparse()

print (sdf.density)

"""

Its output is as follows −

   0.0001

"""
