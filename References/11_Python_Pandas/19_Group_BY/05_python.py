


"""

Iterating through Groups
With the groupby object in hand, we can iterate through the object similar to itertools.obj.



"""


# import the pandas library
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')

for name,group in grouped:
    print (name)
    print (group)

"""

Its output is as follows −

2014
   Points  Rank     Team   Year
0     876     1   Riders   2014
2     863     2   Devils   2014
4     741     3   Kings    2014
9     701     4   Royals   2014

2015
   Points  Rank     Team   Year
1     789     2   Riders   2015
3     673     3   Devils   2015
5     812     4    kings   2015
10    804     1   Royals   2015

2016
   Points  Rank     Team   Year
6     756     1    Kings   2016
8     694     2   Riders   2016

2017
   Points  Rank    Team   Year
7     788     1   Kings   2017
11    690     2  Riders   2017

By default, the groupby object has the same label name as the group name.

"""
