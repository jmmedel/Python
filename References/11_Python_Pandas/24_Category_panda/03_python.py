


"""

Let’s have another example −


"""


import pandas as pd
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print (cat)


"""

Its output is as follows −

[a, b, c, a, b, c, NaN]
Categories (3, object): [c, b, a]
Here, the second argument signifies the categories. Thus, any value which is not present in the categories will be treated as NaN.


"""
