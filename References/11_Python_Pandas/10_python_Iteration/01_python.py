



"""

Python Pandas - Iteration


The behavior of basic iteration over Pandas objects depends on the type. When iterating over a Series, it is regarded as array-like, and basic iteration produces the values. Other data structures, like DataFrame and Panel, follow the dict-like convention of iterating over the keys of the objects.

In short, basic iteration (for i in object) produces −

Series − values

DataFrame − column labels

Panel − item labels

Iterating a DataFrame
Iterating a DataFrame gives column names. Let us consider the following example to understand the same.

"""

import pandas as pd
import numpy as np
 
N=20

df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })

for col in df:
   print (col)
   
"""

Its output is as follows −

A
C
D
x
y
To iterate over the rows of the DataFrame, we can use the following functions −

iteritems() − to iterate over the (key,value) pairs

iterrows() − iterate over the rows as (index,series) pairs

itertuples() − iterate over the rows as namedtuples


"""





