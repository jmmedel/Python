


"""

repeat(value)


"""


import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.repeat(2))

"""

Its output is as follows −

0   Tom            Tom
1   William Rick   William Rick
2                  JohnJohn
3                  Alber@tAlber@t
dtype: object


"""


