

"""
Python 3 - String startswith() Method
Description
The startswith() method checks whether the string starts with str, optionally restricting the matching with the given indices start and end.

Syntax
Following is the syntax for startswith() method −

str.startswith(str, beg = 0,end = len(string));
Parameters
str − This is the string to be checked.

beg − This is the optional parameter to set start index of the matching boundary.

end − This is the optional parameter to set start index of the matching boundary.

Return Value
This method returns true if found matching string otherwise false.

Example
The following example shows the usage of startswith() method."""

str = "this is string example....wow!!!"
print (str.startswith( 'this' ))
print (str.startswith( 'string', 8 ))
print (str.startswith( 'this', 2, 4 ))
