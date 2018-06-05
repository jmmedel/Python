




#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)



"""

Its output is as follows −

100  a
101  b
102  c
103  d
dtype: object
We passed the index values here. Now we can see the customized indexed values in the output.


"""

