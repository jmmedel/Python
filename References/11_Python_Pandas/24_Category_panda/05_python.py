


"""

Description
Using the .describe() command on the categorical data, we get similar output to a Series or DataFrame of the type string.



"""


import pandas as pd
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", np.nan]})
print df.describe()

print (df["cat"].describe())


"""

Its output is as follows −

       cat s
count    3 3
unique   2 2
top      c c
freq     2 2
count     3
unique    2
top       c
freq      2
Name: cat, dtype: object


"""
