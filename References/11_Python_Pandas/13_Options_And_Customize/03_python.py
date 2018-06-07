


"""


set_option(param,value)
set_option takes two arguments and sets the value to the parameter as shown below −

display.max_rows
Using set_option(), we can change the default number of rows to be displayed.


"""


import pandas as pd

pd.set_option("display.max_rows",80)

print (pd.get_option("display.max_rows"))

"""

Its output is as follows −

80


"""
