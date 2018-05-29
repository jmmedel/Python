
"""

Python 3 - dictionary cmp() Method
Advertisements
 Previous Page Next Page  
Description
The method cmp() compares two dictionaries based on key and values.

Syntax
Following is the syntax for cmp() method −

cmp(dict1, dict2)
Parameters
dict1 − This is the first dictionary to be compared with dict2.

dict2 − This is the second dictionary to be compared with dict1.

Return Value
This method returns 0 if both dictionaries are equal, -1 if dict1 < dict2 and 1 if dict1 > dic2.

Example
The following example shows the usage of cmp() method.

"""

dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Name': 'Mahnaz', 'Age': 27}
dict3 = {'Name': 'Abid', 'Age': 27}
dict4 = {'Name': 'Zara', 'Age': 7}
print "Return Value : %d" %  cmp (dict1, dict2)
print "Return Value : %d" %  cmp (dict2, dict3)
print "Return Value : %d" %  cmp (dict1, dict4)
