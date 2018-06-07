


"""

Example 2


"""


import pandas as pd
import numpy as np

# My custom function
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.applymap(lambda x:x*100)
print (df.apply(np.mean))

"""

Its output is as follows −

output is as follows:
         col1         col2         col3
0   17.670426    21.969052    -49.064031
1   22.237846    42.216693     195.392124
2   24.109576   -86.457646     69.643171
3   35.576312   -162.332803   -81.743023
4   30.874333    71.476717     13.028751


"""
