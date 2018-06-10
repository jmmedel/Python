


"""

skiprows
skiprows skips the number of rows specified.



"""


import pandas as pd

df=pd.read_csv("temp.csv", skiprows=2)
print (df)



"""

Its output is as follows −

    2      Lee   32    HongKong   3000
0   3   Steven   43    Bay Area   8300
1   4      Ram   38   Hyderabad   3900


"""
