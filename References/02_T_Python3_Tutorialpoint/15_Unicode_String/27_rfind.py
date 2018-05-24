

"""
Python 3 - String rfind() Method

Description
The rfind() method returns the last index where the substring str is found, or -1 if no such index exists, optionally restricting the search to string[beg:end].

Syntax
Following is the syntax for rfind() method −

str.rfind(str, beg = 0 end = len(string))
Parameters
str − This specifies the string to be searched.

beg − This is the starting index, by default its 0.

end &minus This is the ending index, by default its equal to the length of the string.

Return Value
This method returns last index if found and -1 otherwise.

Example
The following example shows the usage of rfind() method."""

str1 = "this is really a string example....wow!!!"
str2 = "is"

print (str1.rfind(str2))

print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))

print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))

