

"""
ython 3 - String index() Method
Advertisements
 Previous Page Next Page  
Description
The index() method determines if the string str occurs in string or in a substring of string, if the starting index beg and ending index end are given. This method is same as find(), but raises an exception if sub is not found.

Syntax
Following is the syntax for index() method −

str.index(str, beg = 0 end = len(string))
Parameters
str − This specifies the string to be searched.

beg − This is the starting index, by default its 0.

end − This is the ending index, by default its equal to the length of the string.

Return Value
Index if found otherwise raises an exception if str is not found.

Example"""

str1 = "this is string example....wow!!!"
str2 = "exam";

print (str1.index(str2))
print (str1.index(str2, 10))
print (str1.index(str2, 40))
