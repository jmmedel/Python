


"""

Example 2
Let us now create an indexed DataFrame using arrays.


"""


import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print (df)


"""

Its output is as follows −

         Age    Name
rank1    28      Tom
rank2    34     Jack
rank3    29    Steve
rank4    42    Ricky
Note − Observe, the index parameter assigns an index to each row.


"""

