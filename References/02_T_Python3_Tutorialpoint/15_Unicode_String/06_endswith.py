

"""
Python 3 - String endswith() Method
Description
It returns True if the string ends with the specified suffix, otherwise return False optionally restricting the matching with the given indices start and end.

Syntax
str.endswith(suffix[, start[, end]])
Parameters
suffix -- This could be a string or could also be a tuple of suffixes to look for.

start -- The slice begins from here.

end -- The slice ends here.

Return Value
TRUE if the string ends with the specified suffix, otherwise FALSE.

Example"""

Str='this is string example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='exam'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))
