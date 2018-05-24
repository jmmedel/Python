

"""Python 3 - String expandtabs() Method
Advertisements
 Previous Page Next Page  
Description
The expandtabs() method returns a copy of the string in which the tab characters ie. '\t' are expanded using spaces, optionally using the given tabsize (default 8)..

Syntax
Following is the syntax for expandtabs() method −

str.expandtabs(tabsize = 8)
Parameters
tabsize − This specifies the number of characters to be replaced for a tab character '\t'.

Return Value
This method returns a copy of the string in which tab characters i.e., '\t' have been expanded using spaces.

Example"""

str = "this is\tstring example....wow!!!"


print ("Original string: " + str)
print ("Defualt exapanded tab: " +  str.expandtabs())
print ("Double exapanded tab: " +  str.expandtabs(16))


