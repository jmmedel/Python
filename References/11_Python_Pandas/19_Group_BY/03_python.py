


"""

View Groups


"""



# import the pandas library
import pandas as pd
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],           'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print (df.groupby('Team').groups)

"""

Its output is as follows −

{'Kings': Int64Index([4, 6, 7],      dtype='int64'),
'Devils': Int64Index([2, 3],         dtype='int64'),
'Riders': Int64Index([0, 1, 8, 11],  dtype='int64'),
'Royals': Int64Index([9, 10],        dtype='int64'),
'kings' : Int64Index([5],            dtype='int64')}


"""

