"""
Python 3 - Number fabs() Method
Description
The fabs() method returns the absolute value of x. Although similar to the abs() function, there are differences between the two functions. They are −

abs() is a built in function whereas fabs() is defined in math module.

fabs() function works only on float and integer whereas abs() works with complex number also.

Syntax
Following is the syntax for the fabs() method −

import math

math.fabs( x )
Note − This function is not accessible directly, so we need to import the math module and then we need to call this function using the math static object.

Parameters
x − This is a numeric value.

Return Value
This method returns the absolute value of x.

Example
The following example shows the usage of the fabs() method."""

import math   # This will import math module

print ("math.fabs(-45.17) : ", math.fabs(-45.17))
print ("math.fabs(100.12) : ", math.fabs(100.12))
print ("math.fabs(100.72) : ", math.fabs(100.72))
print ("math.fabs(math.pi) : ", math.fabs(math.pi))

