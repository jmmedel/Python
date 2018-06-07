


"""

Python Pandas - Window Functions

For working on numerical data, Pandas provide few variants like rolling, expanding and exponentially moving weights for window statistics. Among these are sum, mean, median, variance, covariance, correlation, etc.

We will now learn how each of these can be applied on DataFrame objects.

.rolling() Function
This function can be applied on a series of data. Specify the window=n argument and apply the appropriate statistical function on top of it.

"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
index = pd.date_range('1/1/2000', periods=10),
columns = ['A', 'B', 'C', 'D'])

print (df.rolling(window=3).mean())


"""

Its output is as follows −

                    A           B           C           D
2000-01-01        NaN         NaN         NaN         NaN
2000-01-02        NaN         NaN         NaN         NaN
2000-01-03   0.434553   -0.667940   -1.051718   -0.826452
2000-01-04   0.628267   -0.047040   -0.287467   -0.161110
2000-01-05   0.398233    0.003517    0.099126   -0.405565
2000-01-06   0.641798    0.656184   -0.322728    0.428015
2000-01-07   0.188403    0.010913   -0.708645    0.160932
2000-01-08   0.188043   -0.253039   -0.818125   -0.108485
2000-01-09   0.682819   -0.606846   -0.178411   -0.404127
2000-01-10   0.688583    0.127786    0.513832   -1.067156
Note − Since the window size is 3, for first two elements there are nulls and from third the value will be the average of the n, n-1 and n-2 elements. Thus we can also apply various functions as mentioned above.


"""

