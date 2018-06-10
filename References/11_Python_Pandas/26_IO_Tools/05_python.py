



"""

header_names
Specify the names of the header using the names argument.



"""

import pandas as pd
 
df=pd.read_csv("temp.csv", names=['a', 'b', 'c','d','e'])
print (df)


"""

Its output is as follows −

       a        b    c           d        e
0   S.No     Name   Age       City   Salary
1      1      Tom   28     Toronto    20000
2      2      Lee   32    HongKong     3000
3      3   Steven   43    Bay Area     8300
4      4      Ram   38   Hyderabad     3900

Observe, the header names are appended with the custom names, but the header in the file has not been eliminated. Now, we use the header argument to remove that.

If the header is in a row other than the first, pass the row number to header. This will skip the preceding rows.

"""
