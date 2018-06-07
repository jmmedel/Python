


"""

replace(a,b)


"""


import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print s
print ("After replacing @ with $:")
print (s.str.replace('@','$'))

"""

Its output is as follows −

0   Tom
1   William Rick
2   John
3   Alber@t
dtype: object

After replacing @ with $:
0   Tom
1   William Rick
2   John
3   Alber$t
dtype: object


"""
