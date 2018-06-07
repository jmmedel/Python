


"""


It is also possible to convert integer or float epoch times. The default unit for these is nanoseconds (since these are how Timestamps are stored). However, often epochs are stored in another unit which can be specified. Let’s take another example


"""


import pandas as pd
print (pd.Timestamp(1587687255,unit='s'))


"""

Its output is as follows −

2020-04-24 00:14:15


"""
