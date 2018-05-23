"""
Python 3 - Number floor() Method
Description
The floor() method returns the floor of x i.e. the largest integer not greater than x.

Syntax
Following is the syntax for floor() method −

import math

math.floor( x )
Note − This function is not accessible directly, so we need to import the math module and then we need to call this function using the math static object.

Parameters
x − This is a numeric expression.

Return Value
This method returns the largest integer not greater than x.

Example
The following example shows the usage of the floor() method."""

import math   # This will import math module

print ("math.floor(-45.17) : ", math.floor(-45.17))
print ("math.floor(100.12) : ", math.floor(100.12))
print ("math.floor(100.72) : ", math.floor(100.72))
print ("math.floor(math.pi) : ", math.floor(math.pi))
