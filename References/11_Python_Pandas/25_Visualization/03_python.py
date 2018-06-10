



"""


To produce a stacked bar plot, pass stacked=True −


"""


import pandas as pd
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d')
df.plot.bar(stacked=True)
