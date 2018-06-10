



"""

Converters
dtype of the columns can be passed as a dict.



"""


import pandas as pd

df = pd.read_csv("temp.csv", dtype={'Salary': np.float64})
print (df.dtypes)


"""

Its output is as follows −

S.No       int64
Name      object
Age        int64
City      object
Salary   float64
dtype: object


"""
