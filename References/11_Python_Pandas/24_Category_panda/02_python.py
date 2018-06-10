



"""

pd.Categorical
Using the standard pandas Categorical constructor, we can create a category object.

pandas.Categorical(values, categories, ordered)

Let’s take an example −

"""


import pandas as pd
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print (cat)


"""
Its output is as follows −

[a, b, c, a, b, c]
Categories (3, object): [a, b, c]

"""
