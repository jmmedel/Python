"""
Python 3 - Number shuffle() Method
Description
The shuffle() method randomizes the items of a list in place.

Syntax
Following is the syntax for shuffle() method −

shuffle (lst,[random])
Note − This function is not accessible directly, so we need to import shuffle module and then we need to call this function using random static object.

Parameters
lst − This could be a list or tuple.

random − This is an optional 0 argument function returning float between 0.0 - 1.0. Default is None

Return Value
This method returns reshuffled list.

Example
The following example shows the usage of the shuffle() method."""


import random

list = [20, 16, 10, 5];
random.shuffle(list)
print ("Reshuffled list : ",  list)

random.shuffle(list)
print ("Reshuffled list : ",  list)
