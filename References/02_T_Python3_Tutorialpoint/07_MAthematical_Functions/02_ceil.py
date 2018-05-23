"""
Python 3 - Number ceil() Method
Description
The ceil() method returns the ceiling value of x i.e. the smallest integer not less than x.

Syntax
Following is the syntax for the ceil() method −
import math

math.ceil( x )
Note − This function is not accessible directly, so we need to import math module and then we need to call this function using the math static object.

Parameters
x − This is a numeric expression.

Return Value
This method returns the smallest integer not less than x.

Example
The following example shows the usage of the ceil() method."""

import math   # This will import math module

print ("math.ceil(-45.17) : ", math.ceil(-45.17))
print ("math.ceil(100.12) : ", math.ceil(100.12))
print ("math.ceil(100.72) : ", math.ceil(100.72))
print ("math.ceil(math.pi) : ", math.ceil(math.pi) )
