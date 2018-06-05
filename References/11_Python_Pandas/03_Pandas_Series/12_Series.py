

"""


Example 3
If a label is not contained, an exception is raised.

"""

import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve multiple elements
print (s['f'])

"""

Its output is as follows −

…
KeyError: 'f'


"""


