"""
Random Number Functions
Random numbers are used for games, simulations, testing, security, and privacy applications. Python includes the following functions that are commonly used."""


"""
Python 3 - Number choice() Method
Description
The choice() method returns a random item from a list, tuple, or string.

Syntax
Following is the syntax for choice() method −

choice( seq )
Note − This function is not accessible directly, so we need to import the random module and then we need to call this function using the random static object.

Parameters
seq − This could be a list, tuple, or string.

Return Value
This method returns a random item.

Example
The following example shows the usage of the choice() method."""

import random

print ("returns a random number from range(100) : ",random.choice(range(100)))
print ("returns random element from list [1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print ("returns random character from string 'Hello World' : ", random.choice('Hello World'))
