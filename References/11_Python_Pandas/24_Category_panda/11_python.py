


"""

Comparison of Categorical Data
Comparing categorical data with other objects is possible in three cases −

comparing equality (== and !=) to a list-like object (list, Series, array, ...) of the same length as the categorical data.

all comparisons (==, !=, >, >=, <, and <=) of categorical data to another categorical Series, when ordered==True and the categories are the same.

all comparisons of a categorical data to a scalar.

Take a look at the following example −


"""


import pandas as pd

cat = pd.Series([1,2,3]).astype("category", categories=[1,2,3], ordered=True)
cat1 = pd.Series([2,2,2]).astype("category", categories=[1,2,3], ordered=True)

print (cat>cat1)

"""

Its output is as follows −

0  False
1  False
2  True
dtype: bool


"""


