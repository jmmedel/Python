

"""
Python 3 - String find() Method

Description
The find() method determines if the string str occurs in string, or in a substring of string if the starting index beg and ending index end are given.

Syntax
Following is the syntax for find() method −

str.find(str, beg = 0 end = len(string))
Parameters
str − This specifies the string to be searched.

beg − This is the starting index, by default its 0.

end − This is the ending index, by default its equal to the lenght of the string.

Return Value
Index if found and -1 otherwise.

Example"""


str1 = "this is string example....wow!!!"
str2 = "exam";

print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))
