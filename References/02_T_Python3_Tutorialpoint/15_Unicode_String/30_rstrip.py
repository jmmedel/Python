

"""
Python 3 - String rstrip() Method
Advertisements
 Previous Page Next Page  
Description
The rstrip() method returns a copy of the string in which all chars have been stripped from the end of the string (default whitespace characters).

Syntax
Following is the syntax for rstrip() method −

str.rstrip([chars])
Parameters
chars − You can supply what chars have to be trimmed.

Return Value
This method returns a copy of the string in which all chars have been stripped from the end of the string (default whitespace characters).

Example
The following example shows the usage of rstrip() method."""

str = "     this is string example....wow!!!     "
print (str.rstrip())

str = "*****this is string example....wow!!!*****"
print (str.rstrip('*'))
