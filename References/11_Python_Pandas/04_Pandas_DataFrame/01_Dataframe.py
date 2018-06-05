


"""

Python Pandas - DataFrame

A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.

Features of DataFrame
Potentially columns are of different types
Size – Mutable
Labeled axes (rows and columns)
Can Perform Arithmetic operations on rows and columns
Structure
Let us assume that we are creating a data frame with student’s data.

Structure Table
You can think of it as an SQL table or a spreadsheet data representation.

pandas.DataFrame
A pandas DataFrame can be created using the following constructor −

pandas.DataFrame( data, index, columns, dtype, copy)
The parameters of the constructor are as follows −

S.No	Parameter & Description
1	
data

data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame.

2	
index

For the row labels, the Index to be used for the resulting frame is Optional Default np.arrange(n) if no index is passed.

3	
columns

For column labels, the optional default syntax is - np.arrange(n). This is only true if no index is passed.

4	
dtype

Data type of each column.

4	
copy

This command (or whatever it is) is used for copying of data, if the default is False.

Create DataFrame
A pandas DataFrame can be created using various inputs like −

Lists
dict
Series
Numpy ndarrays
Another DataFrame
In the subsequent sections of this chapter, we will see how to create a DataFrame using these inputs.

Create an Empty DataFrame
A basic DataFrame, which can be created is an Empty Dataframe.

Example

"""


#import the pandas library and aliasing as pd
import pandas as pd
df = pd.DataFrame()
print (df)

"""

Its output is as follows −

Empty DataFrame
Columns: []
Index: []


"""
