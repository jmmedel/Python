


"""

SciPy - Basic Functionality


By default, all the NumPy functions have been available through the SciPy namespace. There is no need to import the NumPy functions explicitly, when SciPy is imported. The main object of NumPy is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. In NumPy, dimensions are called as axes. The number of axes is called as rank.

Now, let us revise the basic functionality of Vectors and Matrices in NumPy. As SciPy is built on top of NumPy arrays, understanding of NumPy basics is necessary. As most parts of linear algebra deals with matrices only.

NumPy Vector
A Vector can be created in multiple ways. Some of them are described below.

Converting Python array-like objects to NumPy
Let us consider the following example.


"""


import numpy as np
list = [1,2,3,4]
arr = np.array(list)
print (arr)

"""
The output of the above program will be as follows.

[1 2 3 4]



"""
