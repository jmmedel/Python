
"""
Python 3 - Number seed() Method
Description
The seed() method initializes the basic random number generator. Call this function before calling any other random module function.

Syntax
Following is the syntax for seed() method:

seed ([x], [y])
Note − This function initializes the basic random number generator.

Parameters
x − This is the seed for the next random number. If omitted, then it takes system time to generate the next random number. If x is an int, it is used directly.

y − This is version number (default is 2). str, byte or byte array object gets converted in int. Version 1 used hash() of x.

Return Value
This method does not return any value.

Example
The following example shows the usage of seed() method."""

import random

random.seed()
print ("random number with default seed", random.random())
random.seed(10)
print ("random number with int seed", random.random())
random.seed("hello",2)
print ("random number with string seed", random.random())
