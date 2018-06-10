



"""


Bar Plot
Let us now see what a Bar Plot is by creating one. A bar plot can be created in the following way −


"""



import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar()