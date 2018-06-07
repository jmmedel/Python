



"""


Converting to Timestamps
To convert a Series or list-like object of date-like objects, for example strings, epochs, or a mixture, you can use the to_datetime function. When passed, this returns a Series (with the same index), while a list-like is converted to a DatetimeIndex. Take a look at the following example −


"""


import pandas as pd

print (pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None])))

"""

Its output is as follows −

0  2009-07-31
1  2010-01-10
2         NaT
dtype: datetime64[ns]


NaT means Not a Time (equivalent to NaN)

Let’s take another example.


"""


