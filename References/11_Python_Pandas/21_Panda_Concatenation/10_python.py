


"""

Create a Range of Time


"""


import pandas as pd

print (pd.date_range("11:00", "13:30", freq="30min").time)


"""

Its output is as follows −

[datetime.time(11, 0) datetime.time(11, 30) datetime.time(12, 0)
datetime.time(12, 30) datetime.time(13, 0) datetime.time(13, 30)]


"""
