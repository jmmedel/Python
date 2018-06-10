



"""

Renaming Categories
Renaming categories is done by assigning new values to the series.cat.categoriesseries.cat.categories property.


"""


import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
s.cat.categories = ["Group %s" % g for g in s.cat.categories]

print (s.cat.categories)


"""

Its output is as follows −

Index([u'Group a', u'Group b', u'Group c'], dtype='object')
Initial categories [a,b,c] are updated by the s.cat.categories property of the object.


"""
