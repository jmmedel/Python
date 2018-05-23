"""
Python 3 - modf() Method
Description
The modf() method returns the fractional and integer parts of x in a two-item tuple. Both parts have the same sign as x. The integer part is returned as a float.

Syntax
Following is the syntax for the modf() method

import math

math.modf( x )
Note − This function is not accessible directly, so we need to import the math module and then we need to call this function using the math static object.

Parameters
x − This is a numeric expression.

Return Value
This method returns the fractional and integer parts of x in a two-item tuple. Both the parts have the same sign as x. The integer part is returned as a float.

Example
The following example shows the usage of the modf() method."""

import math   # This will import math module

print ("math.modf(100.12) : ", math.modf(100.12))
print ("math.modf(100.72) : ", math.modf(100.72))
print ("math.modf(119) : ", math.modf(119))
print ("math.modf(math.pi) : ", math.modf(math.pi))

