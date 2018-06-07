


"""

Python Pandas - Date Functionality

Extending the Time series, Date functionalities play major role in financial data analysis. While working with Date data, we will frequently come across the following −

Generating sequence of dates
Convert the date series to different frequencies
Create a Range of Dates
Using the date.range() function by specifying the periods and the frequency, we can create the date series. By default, the frequency of range is Days.

"""


import pandas as pd
print (pd.date_range('1/1/2011', periods=5))



"""

Its output is as follows −

DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04', '2011-01-05'],
dtype='datetime64[ns]', freq='D')


"""
