
"""
Python 3 - List extend() Method
Description
The extend() method appends the contents of seq to list.

Syntax
Following is the syntax for extend() method −

list.extend(seq)
Parameters
seq − This is the list of elements

Return Value
This method does not return any value but add the content to existing list.

Example
The following example shows the usage of extend() method."""

list1 = ['physics', 'chemistry', 'maths']
list2=list(range(5)) #creates list of numbers between 0-4
list1.extend(list2)
print ('Extended List :', list1)



