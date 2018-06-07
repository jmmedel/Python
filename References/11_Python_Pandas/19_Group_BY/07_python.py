


"""

Aggregations
An aggregated function returns a single aggregated value for each group. Once the group by object is created, several aggregation operations can be performed on the grouped data.

An obvious one is aggregation via the aggregate or equivalent agg method −



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

grouped = df.groupby('Year')
print (grouped['Points'].agg(np.mean))


"""

Its output is as follows −

Year
2014   795.25
2015   769.50
2016   725.00
2017   739.00
Name: Points, dtype: float64
Another way to see the size of each group is by applying the size() function −

"""

