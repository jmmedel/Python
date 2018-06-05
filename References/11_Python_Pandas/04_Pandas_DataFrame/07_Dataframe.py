


"""

Create a DataFrame from List of Dicts
List of Dictionaries can be passed as input data to create a DataFrame. The dictionary keys are by default taken as column names.

Example 1
The following example shows how to create a DataFrame by passing a list of dictionaries.

"""


import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)

"""

Its output is as follows −

    a    b      c
0   1   2     NaN
1   5   10   20.0
Note − Observe, NaN (Not a Number) is appended in missing areas.


"""
