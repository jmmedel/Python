



"""

.ewm() Function
ewm is applied on a series of data. Specify any of the com, span, halflife argument and apply the appropriate statistical function on top of it. It assigns the weights exponentially.



"""


import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print (df.ewm(com=0.5).mean())


"""

Its output is as follows −

                    A           B           C           D
2000-01-01   1.088512   -0.650942   -2.547450   -0.566858
2000-01-02   0.865131   -0.453626   -1.137961    0.058747
2000-01-03  -0.132245   -0.807671   -0.308308   -1.491002
2000-01-04   1.084036    0.555444   -0.272119    0.480111
2000-01-05   0.425682    0.025511    0.239162   -0.153290
2000-01-06   0.245094    0.671373   -0.725025    0.163310
2000-01-07   0.288030   -0.259337   -1.183515    0.473191
2000-01-08   0.162317   -0.771884   -0.285564   -0.692001
2000-01-09   1.147156   -0.302900    0.380851   -0.607976
2000-01-10   0.600216    0.885614    0.569808   -1.110113
Window functions are majorly used in finding the trends within the data graphically by smoothing the curve. If there is lot of variation in the everyday data and a lot of data points are available, then taking the samples and plotting is one method and applying the window computations and plotting the graph on the results is another method. By these methods, we can smooth the curve or the trend.


"""