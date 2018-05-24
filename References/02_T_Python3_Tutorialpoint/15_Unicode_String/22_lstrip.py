
"""
Python 3 - String lstrip() Method
Advertisements
 Previous Page Next Page  
Description
The lstrip() method returns a copy of the string in which all chars have been stripped from the beginning of the string (default whitespace characters).

Syntax
Following is the syntax for lstrip() method −

str.lstrip([chars])
Parameters
chars − You can supply what chars have to be trimmed.

Return Value
This method returns a copy of the string in which all chars have been stripped from the beginning of the string (default whitespace characters).

Example
The following example shows the usage of lstrip() method."""


str = "     this is string example....wow!!!"
print (str.lstrip())

str = "*****this is string example....wow!!!*****"
print (str.lstrip('*'))
