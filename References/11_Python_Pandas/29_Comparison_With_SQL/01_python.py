


"""

Python Pandas - Comparison with SQL

Since many potential Pandas users have some familiarity with SQL, this page is meant to provide some examples of how various SQL operations can be performed using pandas.

"""


import pandas as pd
url = 'https://raw.github.com/pandasdev/pandas/master/pandas/tests/data/tips.csv'
tips=pd.read_csv(url)
print (tips.head())


"""

Its output is as follows −

    total_bill   tip      sex  smoker  day     time  size
0        16.99  1.01   Female      No  Sun  Dinner      2
1        10.34  1.66     Male      No  Sun  Dinner      3
2        21.01  3.50     Male      No  Sun  Dinner      3
3        23.68  3.31     Male      No  Sun  Dinner      2
4        24.59  3.61   Female      No  Sun  Dinner      4



"""

