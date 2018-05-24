
"""
Python 3 - String replace() Method
Advertisements
 Previous Page Next Page  
Description
The replace() method returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to max.

Syntax
Following is the syntax for replace() method −

str.replace(old, new[, max])
Parameters
old − This is old substring to be replaced.

new − This is new substring, which would replace old substring.

max − If this optional argument max is given, only the first count occurrences are replaced.

Return Value
This method returns a copy of the string with all occurrences of substring old replaced by new. If the optional argument max is given, only the first count occurrences are replaced.

Example
The following example shows the usage of replace() method."""


str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))
