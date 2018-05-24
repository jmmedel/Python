"""
Python 3 - String count() Method
Description
The count() method returns the number of occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

Syntax
Following is the syntax for count() method −

str.count(sub, start = 0,end = len(string))
Parameters
sub − This is the substring to be searched.

start − Search starts from this index. First character starts from 0 index. By default search starts from 0 index.

end − Search ends from this index. First character starts from 0 index. By default search ends at the last index.

Return Value
Centered in a string of length width."""

str = "this is string example....wow!!!"
sub = 'i'
print ("str.count('i') : ", str.count(sub))
sub = 'exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))
