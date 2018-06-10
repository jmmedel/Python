


"""

Removing Categories
Using the Categorical.remove_categories() method, unwanted categories can be removed.


"""


import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
print ("Original object:")
print s

print ("After removal:")
print (s.cat.remove_categories("a"))


"""

Its output is as follows −

Original object:
0  a
1  b
2  c
3  a
dtype: category
Categories (3, object): [a, b, c]

After removal:
0  NaN
1  b
2  c
3  NaN
dtype: category
Categories (2, object): [b, c]


"""
