


"""

Appending New Categories
Using the Categorical.add.categories() method, new categories can be appended.



"""


import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
s = s.cat.add_categories([4])
print (s.cat.categories)


"""

Its output is as follows −

Index([u'a', u'b', u'c', 4], dtype='object')


"""
