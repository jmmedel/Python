


"""


Example 2
The following example shows how to create a DataFrame by passing a list of dictionaries and the row indices.

"""


import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print (df)
