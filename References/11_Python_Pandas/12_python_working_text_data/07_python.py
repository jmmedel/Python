


"""

cat(sep=pattern)


"""

import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print (s.str.cat(sep='_'))

"""
Its output is as follows −

Tom _ William Rick_John_Alber@t


"""

