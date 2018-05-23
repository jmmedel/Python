"""
Python Number random() Method
Description
The random() method returns a random floating point number in the range [0.0, 1.0].

Syntax
Following is the syntax for the random() method −

random ( )
Note − This function is not accessible directly, so we need to import the random module and then we need to call this function using the random static object.

Parameters
NA

Return Value
This method returns a random float r, such that 0.0 <= r <= 1.0

Example
The following example shows the usage of the random() method."""

import random

# First random number
print ("random() : ", random.random())

# Second random number
print ("random() : ", random.random())

