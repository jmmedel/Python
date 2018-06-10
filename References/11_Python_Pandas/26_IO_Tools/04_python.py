


import pandas as pd

df = pd.read_csv("temp.csv", dtype={'Salary': np.float64})
print df.dtypes

"""


By default, the dtype of the Salary column is int, but the result shows it as float because we have explicitly casted the type.

Thus, the data looks like float −

S.No   Name   Age      City    Salary
0   1     Tom   28    Toronto   20000.0
1   2     Lee   32   HongKong    3000.0
2   3  Steven   43   Bay Area    8300.0
3   4     Ram   38  Hyderabad    3900.0

"""


