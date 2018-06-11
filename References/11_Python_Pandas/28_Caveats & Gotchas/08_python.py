


"""




"""


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
'four'],index=list('abcdef'))

print (df)
print (df.ix[[1, 2, 4]])
print (df.reindex([1, 2, 4]))

"""


Its output is as follows −

          one        two      three       four
a   -1.015695  -0.553847   1.106235  -0.784460
b   -0.527398  -0.518198  -0.710546  -0.512036
c   -0.842803  -1.050374   0.787146   0.205147
d   -1.238016  -0.749554  -0.547470  -0.029045
e   -0.056788   1.063999  -0.767220   0.212476
f    1.139714   0.036159   0.201912   0.710119

          one        two      three       four
b   -0.527398  -0.518198  -0.710546  -0.512036
c   -0.842803  -1.050374   0.787146   0.205147
e   -0.056788   1.063999  -0.767220   0.212476

    one  two  three  four
1   NaN  NaN    NaN   NaN
2   NaN  NaN    NaN   NaN
4   NaN  NaN    NaN   NaN
It is important to remember that reindex is strict label indexing only. This can lead to some potentially surprising results in pathological cases where an index contains, say, both integers and strings.


"""
