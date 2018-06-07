


"""

endswith(pattern)

"""

import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print ("Strings that end with 't':")
print (s.str.endswith('t'))



"""

Its output is as follows −

Strings that end with 't':
0  False
1  False
2  False
3  True
dtype: bool


"""
