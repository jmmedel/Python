



"""

to_timedelta()
Using the top-level pd.to_timedelta, you can convert a scalar, array, list, or series from a recognized timedelta format/ value into a Timedelta type. It will construct Series if the input is a Series, a scalar if the input is scalar-like, otherwise will output a TimedeltaIndex.



"""

import pandas as pd

print (pd.Timedelta(days=2))


"""

Its output is as follows −

2 days 00:00:00


"""


