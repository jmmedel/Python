


"""

Python Pandas - Panel


A panel is a 3D container of data. The term Panel data is derived from econometrics and is partially responsible for the name pandas − pan(el)-da(ta)-s.

The names for the 3 axes are intended to give some semantic meaning to describing operations involving panel data. They are −

items − axis 0, each item corresponds to a DataFrame contained inside.

major_axis − axis 1, it is the index (rows) of each of the DataFrames.

minor_axis − axis 2, it is the columns of each of the DataFrames.

pandas.Panel()
A Panel can be created using the following constructor −

pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
The parameters of the constructor are as follows −

Parameter	Description
data	Data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame
items	axis=0
major_axis	axis=1
minor_axis	axis=2
dtype	Data type of each column
copy	Copy data. Default, false
Create Panel
A Panel can be created using multiple ways like −

From ndarrays
From dict of DataFrames
From 3D ndarray

"""


# creating an empty panel
import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
p = pd.Panel(data)
print (p)

"""

Its output is as follows −

<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 5 (minor_axis)
Items axis: 0 to 1
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 4


Note − Observe the dimensions of the empty panel and the above panel, all the objects are different.

"""
