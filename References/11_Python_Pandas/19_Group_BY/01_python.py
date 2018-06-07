


"""


Python Pandas - GroupBy

Any groupby operation involves one of the following operations on the original object. They are −

Splitting the Object

Applying a function

Combining the results

In many situations, we split the data into sets and we apply some functionality on each subset. In the apply functionality, we can perform the following operations −

Aggregation − computing a summary statistic

Transformation − perform some group-specific operation

Filtration − discarding the data with some condition

Let us now create a DataFrame object and perform all the operations on it −

"""

#import the pandas library
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print (df)


"""

Its output is as follows −

    Points   Rank     Team   Year
0      876      1   Riders   2014
1      789      2   Riders   2015
2      863      2   Devils   2014
3      673      3   Devils   2015
4      741      3    Kings   2014
5      812      4    kings   2015
6      756      1    Kings   2016
7      788      1    Kings   2017
8      694      2   Riders   2016
9      701      4   Royals   2014
10     804      1   Royals   2015
11     690      2   Riders   2017


"""

