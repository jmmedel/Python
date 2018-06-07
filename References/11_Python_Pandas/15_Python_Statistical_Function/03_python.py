


"""

Covariance method when applied on a DataFrame, computes cov between all the columns.


"""
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print (frame['a'].cov(frame['b']))
print (frame.cov())



"""

Its output is as follows −

-0.58312921152741437

           a           b           c           d            e
a   1.780628   -0.583129   -0.185575    0.003679    -0.136558
b  -0.583129    1.297011    0.136530   -0.523719     0.251064
c  -0.185575    0.136530    0.915227   -0.053881    -0.058926
d   0.003679   -0.523719   -0.053881    1.521426    -0.487694
e  -0.136558    0.251064   -0.058926   -0.487694     0.960761
Note − Observe the cov between a and b column in the first statement and the same is the value returned by cov on DataFrame.



"""
