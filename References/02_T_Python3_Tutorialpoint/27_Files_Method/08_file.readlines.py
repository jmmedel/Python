

"""

Python 3 - File readlines() Method
Advertisements
 Previous Page Next Page  
Description
The method readlines() reads until EOF using readline() and returns a list containing the lines. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.

An empty string is returned only when EOF is encountered immediately.

Syntax
Following is the syntax for readlines() method −

fileObject.readlines( sizehint );
Parameters
sizehint − This is the number of bytes to be read from the file.

Return Value
This method returns a list containing the lines.

Example
The following example shows the usage of readlines() method.


"""


# Open a file
fo = open("References/02_T_Python3_Tutorialpoint/27_Files_Method/foo.txt", "r+")
print ("Name of the file: ", fo.name)

line = fo.readlines()
print ("Read Line: %s" % (line))

line = fo.readlines(2)
print ("Read Line: %s" % (line))

# Close opened file
fo.close()

