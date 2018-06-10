


"""

Operations
You can operate on Series/ DataFrames and construct timedelta64[ns] Series through subtraction operations on datetime64[ns] Series, or Timestamps.

Let us now create a DataFrame with Timedelta and datetime objects and perform some arithmetic operations on it −



"""


import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
print (df)



"""

Its output is as follows −

            A      B
0  2012-01-01 0 days
1  2012-01-02 1 days
2  2012-01-03 2 days


"""
