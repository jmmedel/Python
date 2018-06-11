


"""

Caveats means warning and gotcha means an unseen problem.

Using If/Truth Statement with Pandas
Pandas follows the numpy convention of raising an error when you try to convert something to a bool. This happens in an if or when using the Boolean operations, and, or, or not. It is not clear what the result should be. Should it be True because it is not zerolength? False because there are False values? It is unclear, so instead, Pandas raises a ValueError 



"""

import pandas as pd

if pd.Series([False, True, False]):
   print ('I am True')


"""

Its output is as follows −

ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool() a.item(), a.an

"""