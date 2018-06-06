


"""

Using minor_axis
Data can be accessed using the method panel.minor_axis(index).


"""

# creating an empty panel
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print (p.minor_xs(1))

"""
Its output is as follows −

       Item1       Item2
0   -0.128637   -1.047032
1    0.896681   -0.557322
2    0.571668    0.431953
3   -0.144234    1.302466
Note − Observe the changes in the dimensions.



"""



