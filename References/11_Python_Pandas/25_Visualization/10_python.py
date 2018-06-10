


"""


Pie Chart
Pie chart can be created using the DataFrame.plot.pie() method.


"""


import pandas as pd
import numpy as np

df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)
