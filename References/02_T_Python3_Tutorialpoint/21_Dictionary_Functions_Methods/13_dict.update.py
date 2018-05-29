

"""
Python 3 - dictionary update() Method
Advertisements
 Previous Page Next Page  
Description
The method update() adds dictionary dict2's key-values pairs in to dict. This function does not return anything.

Syntax
Following is the syntax for update() method −

dict.update(dict2)
Parameters
dict2 − This is the dictionary to be added into dict.

Return Value
This method does not return any value.

Example
The following example shows the usage of update() method.


"""


dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }

dict.update(dict2)
print ("updated dict : ", dict)
