


"""

Python Pandas - Series
Advertisements
 Previous Page Next Page  
Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). The axis labels are collectively called index.

pandas.Series
A pandas Series can be created using the following constructor −

pandas.Series( data, index, dtype, copy)
The parameters of the constructor are as follows −

S.No	Parameter & Description
1	
data

data takes various forms like ndarray, list, constants

2	
index

Index values must be unique and hashable, same length as data. Default np.arrange(n) if no index is passed.

3	
dtype

dtype is for data type. If None, data type will be inferred

4	
copy

Copy data. Default False

A series can be created using various inputs like −

Array
Dict
Scalar value or constant
Create an Empty Series
A basic series, which can be created is an Empty Series.

Example

#import the pandas library and aliasing as pd
import pandas as pd
s = pd.Series()
print s
Its output is as follows −

Series([], dtype: float64)

"""

#import the pandas library and aliasing as pd
import pandas as pd
s = pd.Series()
print (s)

