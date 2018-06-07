


"""

Python Pandas - Options and Customization

Pandas provide API to customize some aspects of its behavior, display is being mostly used.

The API is composed of five relevant functions. They are −

get_option()
set_option()
reset_option()
describe_option()
option_context()
Let us now understand how the functions operate.

get_option(param)
get_option takes a single parameter and returns the value as given in the output below −

display.max_rows
Displays the default number of value. Interpreter reads this value and displays the rows with this value as upper limit to display.


"""


"""


"""

import pandas as pd
print (pd.get_option("display.max_rows"))


"""

Its output is as follows −

60


"""



