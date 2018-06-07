


"""

count(pattern)


"""


import pandas as pd
 
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print ("The number of 'm's in each string:")
print s.str.count('m')


"""

Its output is as follows −

The number of 'm's in each string:
0    1
1    1
2    0
3    0


"""



