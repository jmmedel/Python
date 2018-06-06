


"""

Using major_axis
Data can be accessed using the method panel.major_axis(index).



"""


# creating an empty panel
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p.major_xs(1)


"""

Its output is as follows −

      Item1       Item2
0   0.417497    0.748412
1   0.896681   -0.557322
2   0.576657       NaN


"""

