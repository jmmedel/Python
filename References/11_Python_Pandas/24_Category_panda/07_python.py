
import pandas as pd
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print (cat.ordered)



"""

Its output is as follows −

False


"""

