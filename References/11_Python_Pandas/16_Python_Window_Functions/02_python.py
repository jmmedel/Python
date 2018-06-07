


"""

.expanding() Function
This function can be applied on a series of data. Specify the min_periods=n argument and apply the appropriate statistical function on top of it.


"""


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print (df.expanding(min_periods=3).mean())


"""

Its output is as follows −

                   A           B           C           D
2000-01-01        NaN         NaN         NaN         NaN
2000-01-02        NaN         NaN         NaN         NaN
2000-01-03   0.434553   -0.667940   -1.051718   -0.826452
2000-01-04   0.743328   -0.198015   -0.852462   -0.262547
2000-01-05   0.614776   -0.205649   -0.583641   -0.303254
2000-01-06   0.538175   -0.005878   -0.687223   -0.199219
2000-01-07   0.505503   -0.108475   -0.790826   -0.081056
2000-01-08   0.454751   -0.223420   -0.671572   -0.230215
2000-01-09   0.586390   -0.206201   -0.517619   -0.267521
2000-01-10   0.560427   -0.037597   -0.399429   -0.376886


"""
