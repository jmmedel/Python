

"""
Python 3 - List pop() Method
Description
The pop() method removes and returns last object or obj from the list.

Syntax
Following is the syntax for pop() method −

list.pop(obj = list[-1])
Parameters
obj − This is an optional parameter, index of the object to be removed from the list.

Return Value
This method returns the removed object from the list.

Example
The following example shows the usage of pop() method."""

list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.pop()
print ("list now : ", list1)
list1.pop(1)
print ("list now : ", list1)
