


"""

To get horizontal bar plots, use the barh method −



"""


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d')

df.plot.barh(stacked=True)

