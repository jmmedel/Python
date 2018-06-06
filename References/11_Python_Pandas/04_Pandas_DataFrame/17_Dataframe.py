


"""

Addition of Rows
Add new rows to a DataFrame using the append function. This function will append the rows at the end.



"""


import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print (df)


"""


Its output is as follows −

   a  b
0  1  2
1  3  4
0  5  6
1  7  8

"""
