



"""

Get the Properties of the Category
obj.cat.categories command is used to get the categories of the object.



"""


import pandas as pd
import numpy as np

s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print (s.categories)


"""

Its output is as follows −

Index([u'b', u'a', u'c'], dtype='object')
obj.ordered command is used to get the order of the object.

"""



