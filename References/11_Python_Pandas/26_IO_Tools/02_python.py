


"""

custom index
This specifies a column in the csv file to customize the index using index_col.



"""


import pandas as pd

df=pd.read_csv("temp.csv",index_col=['S.No'])
print (df)

"""

Its output is as follows −

S.No   Name   Age       City   Salary
1       Tom    28    Toronto    20000
2       Lee    32   HongKong     3000
3    Steven    43   Bay Area     8300
4       Ram    38  Hyderabad     3900

"""

