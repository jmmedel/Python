
"""

Python 3 - dictionary fromkeys() Method
Advertisements
 Previous Page Next Page  
Description
The method fromkeys() creates a new dictionary with keys from seq and values set to value.

Syntax
Following is the syntax for fromkeys() method −

dict.fromkeys(seq[, value]))
Parameters
seq − This is the list of values which would be used for dictionary keys preparation.

value − This is optional, if provided then value would be set to this value

Return Value
This method returns the list.

"""

seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print ("New Dictionary : %s" %  str(dict))

dict = dict.fromkeys(seq, 10)
print ("New Dictionary : %s" %  str(dict))

