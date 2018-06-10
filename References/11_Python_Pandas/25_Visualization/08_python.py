


"""


Area Plot
Area plot can be created using the Series.plot.area() or the DataFrame.plot.area() methods.


"""


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area()
