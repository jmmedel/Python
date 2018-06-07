



"""

Data Ranking
Data Ranking produces ranking for each element in the array of elements. In case of ties, assigns the mean rank.



"""

import pandas as pd
import numpy as np
s = pd.Series(np.random.np.random.randn(5), index=list('abcde'))

s['d'] = s['b'] # so there's a tie

print (s.rank())


"""

Its output is as follows −

a  1.0
b  3.5
c  2.0
d  3.5
e  5.0
dtype: float64
Rank optionally takes a parameter ascending which by default is true; when false, data is reverse-ranked, with larger values assigned a smaller rank.

Rank supports different tie-breaking methods, specified with the method parameter −

average − average rank of tied group

min − lowest rank in the group

max − highest rank in the group

first − ranks assigned in the order they appear in the array

"""



