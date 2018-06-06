



"""


Selecting the Data from Panel
Select the data from the panel using −

Items
Major_axis
Minor_axis


"""

# creating an empty panel
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print (p['Item1'])


"""

Its output is as follows −

            0          1          2
0    0.488224  -0.128637   0.930817
1    0.417497   0.896681   0.576657
2   -2.775266   0.571668   0.290082
3   -0.400538  -0.144234   1.110535
We have two items, and we retrieved item1. The result is a DataFrame with 4 rows and 3 columns, which are the Major_axis and Minor_axis dimensions.


"""

