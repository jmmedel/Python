


"""

display.max_rows
Using set_option(), we can change the default number of rows to be displayed.

"""

import pandas as pd

pd.set_option("display.max_columns",30)

print (pd.get_option("display.max_columns"))

"""

Its output is as follows −

30

"""
