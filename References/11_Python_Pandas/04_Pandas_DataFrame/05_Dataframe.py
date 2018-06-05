


"""

Create a DataFrame from Dict of ndarrays / Lists
All the ndarrays must be of same length. If index is passed, then the length of the index should equal to the length of the arrays.

If no index is passed, then by default, index will be range(n), where n is the array length.

Example 1


"""

import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)



"""

Its output is as follows −

      Age      Name
0     28        Tom
1     34       Jack
2     29      Steve
3     42      Ricky
Note − Observe the values 0,1,2,3. They are the default index assigned to each using the function range(n).


"""
