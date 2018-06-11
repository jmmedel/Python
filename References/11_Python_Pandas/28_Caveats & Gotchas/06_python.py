


"""

Reindexing vs ix Gotcha
Many users will find themselves using the ix indexing capabilities as a concise means of selecting data from a Pandas object −


"""


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
'four'],index=list('abcdef'))

print (df)
print (df.ix[['b', 'c', 'e']])


"""

Its output is as follows −

          one        two      three       four
a   -1.582025   1.335773   0.961417  -1.272084
b    1.461512   0.111372  -0.072225   0.553058
c   -1.240671   0.762185   1.511936  -0.630920
d   -2.380648  -0.029981   0.196489   0.531714
e    1.846746   0.148149   0.275398  -0.244559
f   -1.842662  -0.933195   2.303949   0.677641

          one        two      three       four
b    1.461512   0.111372  -0.072225   0.553058
c   -1.240671   0.762185   1.511936  -0.630920
e    1.846746   0.148149   0.275398  -0.244559



"""
