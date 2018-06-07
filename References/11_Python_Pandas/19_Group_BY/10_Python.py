


"""

Transformations

Transformation on a group or a column returns an object that is indexed the same size of that is being grouped. Thus, the transform should return a result that is the same size as that of a group chunk.


"""


# import the pandas library
import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Team')
score = lambda x: (x - x.mean()) / x.std()*10
print (grouped.transform(score))


"""

Its output is as follows −

       Points        Rank        Year
0   12.843272  -15.000000  -11.618950
1   3.020286     5.000000   -3.872983
2   7.071068    -7.071068   -7.071068
3  -7.071068     7.071068    7.071068
4  -8.608621    11.547005  -10.910895
5        NaN          NaN         NaN
6  -2.360428    -5.773503    2.182179
7  10.969049    -5.773503    8.728716
8  -7.705963     5.000000    3.872983
9  -7.071068     7.071068   -7.071068
10  7.071068    -7.071068    7.071068
11 -8.157595     5.000000   11.618950



"""
