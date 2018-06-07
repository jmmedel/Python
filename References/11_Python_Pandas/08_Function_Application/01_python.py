


"""


Python Pandas - Function Application

To apply your own or another library’s functions to Pandas objects, you should be aware of the three important methods. The methods have been discussed below. The appropriate method to use depends on whether your function expects to operate on an entire DataFrame, row- or column-wise, or element wise.

Table wise Function Application: pipe()
Row or Column Wise Function Application: apply()
Element wise Function Application: applymap()
Table-wise Function Application
Custom operations can be performed by passing the function and the appropriate number of parameters as pipe arguments. Thus, operation is performed on the whole DataFrame.

For example, add a value 2 to all the elements in the DataFrame. Then,

adder function
The adder function adds two numeric values as parameters and returns the sum.

def adder(ele1,ele2):
return ele1+ele2
We will now use the custom function to conduct operation on the DataFrame.

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
Let’s see the full program −

"""


import pandas as pd
import numpy as np

def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
print (df.apply(np.mean))


"""

Its output is as follows −

        col1       col2       col3
0   2.176704   2.219691   1.509360
1   2.222378   2.422167   3.953921
2   2.241096   1.135424   2.696432
3   2.355763   0.376672   1.182570
4   2.308743   2.714767   2.130288


"""

