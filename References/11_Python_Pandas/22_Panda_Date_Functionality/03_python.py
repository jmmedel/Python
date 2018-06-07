


"""

bdate_range
bdate_range() stands for business date ranges. Unlike date_range(), it excludes Saturday and Sunday.



"""


import pandas as pd
print (pd.date_range('1/1/2011', periods=5))


"""

Its output is as follows −

DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04', '2011-01-05'],
dtype='datetime64[ns]', freq='D')


"""
