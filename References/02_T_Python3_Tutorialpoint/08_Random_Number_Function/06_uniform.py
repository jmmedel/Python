"""
Python 3 - Number uniform() Method
Description
The uniform() method returns a random float r, such that x is less than or equal to r and r is less than y.

Syntax
Following is the syntax for the uniform() method −

uniform(x, y)
Note − This function is not accessible directly, so we need to import uniform module and then we need to call this function using random static object.

Parameters
x − Sets the lower limit of the random float.

y − Sets the upper limit of the random float.

Return Value
This method returns a floating point number r such that x <= r < y.

Example
The following example shows the usage of uniform() method"""

import random

print ("Random Float uniform(5, 10) : ",  random.uniform(5, 10))

print ("Random Float uniform(7, 14) : ",  random.uniform(7, 14))

