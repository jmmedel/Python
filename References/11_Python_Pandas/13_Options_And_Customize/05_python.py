


"""

reset_option(param)
reset_option takes an argument and sets the value back to the default value.

display.max_rows
Using reset_option(), we can change the value back to the default number of rows to be displayed


"""

import pandas as pd

pd.reset_option("display.max_rows")
print (pd.get_option("display.max_rows"))


"""

Its output is as follows −

60

"""
