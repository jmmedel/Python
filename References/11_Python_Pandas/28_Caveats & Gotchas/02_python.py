

"""

In if condition, it is unclear what to do with it. The error is suggestive of whether to use a None or any of those



"""

import pandas as pd
if pd.Series([False, True, False]).any():
   print("I am any")


"""

Its output is as follows −

I am any

"""
