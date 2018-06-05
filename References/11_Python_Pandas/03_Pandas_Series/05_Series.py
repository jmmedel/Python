

#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print (s)




"""

Its output is as follows −

b 1.0
c 2.0
d NaN
a 0.0
dtype: float64

Observe − Index order is persisted and the missing element is filled with NaN (Not a Number).


"""
