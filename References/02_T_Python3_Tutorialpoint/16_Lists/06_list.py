

"""
Python 3 - List list() Method

Description
The list() method takes sequence types and converts them to lists. This is used to convert a given tuple into list.

Note − Tuple are very similar to lists with only difference that element values of a tuple can not be changed and tuple elements are put between parentheses instead of square bracket. This function also converts characters in a string into a list.

Syntax
Following is the syntax for list() method −

list( seq )
Parameters
seq − This is a tuple or string to be converted into list.

Return Value
This method returns the list.

Example
The following example shows the usage of list() method."""

aTuple = (123, 'C++', 'Java', 'Python')
list1 = list(aTuple)
print ("List elements : ", list1)

str="Hello World"

list2=list(str)
print ("List elements : ", list2)
