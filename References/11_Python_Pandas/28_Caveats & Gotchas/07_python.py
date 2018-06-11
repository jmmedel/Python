


"""

This is, of course, completely equivalent in this case to using the reindex method −



"""

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
'four'],index=list('abcdef'))
print (df)
print (df.reindex(['b', 'c', 'e']))


"""


Its output is as follows −

          one        two      three       four
a    1.639081   1.369838   0.261287  -1.662003
b   -0.173359   0.242447  -0.494384   0.346882
c   -0.106411   0.623568   0.282401  -0.916361
d   -1.078791  -0.612607  -0.897289  -1.146893
e    0.465215   1.552873  -1.841959   0.329404
f    0.966022  -0.190077   1.324247   0.678064

          one        two      three       four
b   -0.173359   0.242447  -0.494384   0.346882
c   -0.106411   0.623568   0.282401  -0.916361
e    0.465215   1.552873  -1.841959   0.329404


Some might conclude that ix and reindex are 100% equivalent based on this. This is true except in the case of integer indexing. For example, the above operation can alternatively be expressed as −

"""
