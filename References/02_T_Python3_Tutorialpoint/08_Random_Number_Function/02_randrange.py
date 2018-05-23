"""
Python 3 - Number randrange() Method
Description
The randrange() method returns a randomly selected element from range(start, stop, step).

Syntax
Following is the syntax for the randrange() method

randrange ([start,] stop [,step])
Note − This function is not accessible directly, so we need to import the random module and then we need to call this function using the random static object.

Parameters
start − Start point of the range. This would be included in the range. Default is 0

stop − Stop point of the range. This would be included in the range. Default is 1

step − Step point of the range. This would be excluded from the range.

Return Value
This method returns a random item from the given range.

Example
The following example shows the usage of the randrange() method."""

import random

# randomly select an odd number between 1-100 
print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))

# randomly select a number between 0-99 
print ("randrange(100) : ", random.randrange(100))
