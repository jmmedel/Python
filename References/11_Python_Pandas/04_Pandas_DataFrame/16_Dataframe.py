


"""

Slice Rows
Multiple rows can be selected using ‘ : ’ operator.



"""


import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df[2:4])


"""


Its output is as follows −

      one    two
c     3.0     3
d     NaN     4

"""


