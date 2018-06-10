


"""


Scatter Plot
Scatter plot can be created using the DataFrame.plot.scatter() methods.


"""


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')
