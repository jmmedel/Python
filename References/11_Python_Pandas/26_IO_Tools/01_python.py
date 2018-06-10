


"""


Python Pandas - IO Tools

The Pandas I/O API is a set of top level reader functions accessed like pd.read_csv() that generally return a Pandas object.

The two workhorse functions for reading text files (or the flat files) are read_csv() and read_table(). They both use the same parsing code to intelligently convert tabular data into a DataFrame object −

pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer',
names=None, index_col=None, usecols=None
pandas.read_csv(filepath_or_buffer, sep='\t', delimiter=None, header='infer',
names=None, index_col=None, usecols=None
Here is how the csv file data looks like −

S.No,Name,Age,City,Salary
1,Tom,28,Toronto,20000
2,Lee,32,HongKong,3000
3,Steven,43,Bay Area,8300
4,Ram,38,Hyderabad,3900
Save this data as temp.csv and conduct operations on it.

S.No,Name,Age,City,Salary
1,Tom,28,Toronto,20000
2,Lee,32,HongKong,3000
3,Steven,43,Bay Area,8300
4,Ram,38,Hyderabad,3900
Save this data as temp.csv and conduct operations on it.

read.csv
read.csv reads data from the csv files and creates a DataFrame object.

"""


import pandas as pd
df=pd.read_csv("temp.csv")
print (df)

"""

Its output is as follows −

   S.No     Name   Age       City   Salary
0     1      Tom    28    Toronto    20000
1     2      Lee    32   HongKong     3000
2     3   Steven    43   Bay Area     8300
3     4      Ram    38  Hyderabad     3900



"""

