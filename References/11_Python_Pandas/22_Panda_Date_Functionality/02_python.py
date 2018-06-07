


"""

Change the Date Frequency


"""


import pandas as pd
print (pd.date_range('1/1/2011', periods=5,freq='M'))

"""

Its output is as follows −

DatetimeIndex(['2011-01-31', '2011-02-28', '2011-03-31', '2011-04-30', '2011-05-31'],
dtype='datetime64[ns]', freq='M')


"""

