

"""
Python 3 - String rindex() Method
Advertisements
 Previous Page Next Page  
Description
The rindex() method returns the last index where the substring str is found, or raises an exception if no such index exists, optionally restricting the search to string[beg:end].

Syntax
Following is the syntax for rindex() method −

str.rindex(str, beg = 0 end = len(string))
Parameters
str − This specifies the string to be searched.

beg − This is the starting index, by default its 0

len − This is ending index, by default its equal to the length of the string.

Return Value
This method returns last index if found otherwise raises an exception if str is not found.

Example
The following example shows the usage of rindex() method."""

str1 = "this is really a string example....wow!!!"
str2 = "is"

print (str1.rindex(str2))
print (str1.rindex(str2,10))
