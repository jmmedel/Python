


"""


Python Pandas - Categorical Data


Often in real-time, data includes the text columns, which are repetitive. Features like gender, country, and codes are always repetitive. These are the examples for categorical data.

Categorical variables can take on only a limited, and usually fixed number of possible values. Besides the fixed length, categorical data might have an order but cannot perform numerical operation. Categorical are a Pandas data type.

The categorical data type is useful in the following cases −

A string variable consisting of only a few different values. Converting such a string variable to a categorical variable will save some memory.

The lexical order of a variable is not the same as the logical order (“one”, “two”, “three”). By converting to a categorical and specifying an order on the categories, sorting and min/max will use the logical order instead of the lexical order.

As a signal to other python libraries that this column should be treated as a categorical variable (e.g. to use suitable statistical methods or plot types).

Object Creation
Categorical object can be created in multiple ways. The different ways have been described below −

category
By specifying the dtype as "category" in pandas object creation.

"""


import pandas as pd
s = pd.Series(["a","b","c","a"], dtype="category")
print (s)


"""

Its output is as follows −

0  a
1  b
2  c
3  a
dtype: category
Categories (3, object): [a, b, c]

The number of elements passed to the series object is four, but the categories are only three. Observe the same in the output Categories.
"""


