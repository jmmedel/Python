


"""

Python Pandas - Visualization


Basic Plotting: plot
This functionality on Series and DataFrame is just a simple wrapper around the matplotlib libraries plot() method.

"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
   periods=10), columns=list('ABCD'))

df.plot()


"""

If the index consists of dates, it calls gct().autofmt_xdate() to format the x-axis as shown in the above illustration.

We can plot one column versus another using the x and y keywords.

Plotting methods allow a handful of plot styles other than the default line plot. These methods can be provided as the kind keyword argument to plot(). These include −

bar or barh for bar plots
hist for histogram
box for boxplot
'area' for area plots
'scatter' for scatter plots


"""
