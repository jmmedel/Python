

"""
Python 3 - String rjust() Method
Advertisements
 Previous Page Next Page  
Description
The rjust() method returns the string right justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than len(s).

Syntax
Following is the syntax for rjust() method −

str.rjust(width[, fillchar])
Parameters
width − This is the string length in total after padding.

fillchar − This is the filler character, default is a space.

Return Value
This method returns the string right justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than len(s).

Example
The following example shows the usage of rjust() method."""

str = "this is string example....wow!!!"
print (str.rjust(50, '*'))
