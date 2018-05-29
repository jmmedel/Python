

"""


Python 3 - File readline() Method
Advertisements
 Previous Page Next Page  
Description
The method readline()reads one entire line from the file. A trailing newline character is kept in the string. If the size argument is present and non-negative, it is a maximum byte count including the trailing newline and an incomplete line may be returned.

An empty string is returned only when EOF is encountered immediately.

Syntax
Following is the syntax for readline() method −

fileObject.readline( size );
Parameters
size − This is the number of bytes to be read from the file.

Return Value
This method returns the line read from the file.

Example
The following example shows the usage of readline() method.

"""

# Open a file
fo = open("References/02_T_Python3_Tutorialpoint/27_Files_Method/foo.txt", "r+")
print ("Name of the file: ", fo.name)

line = fo.readline()
print ("Read Line: %s" % (line))

line = fo.readline(5)
print ("Read Line: %s" % (line))

# Close opened file
fo.close()

