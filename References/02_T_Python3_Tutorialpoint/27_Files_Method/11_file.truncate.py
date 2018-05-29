

"""

Python 3 - File truncate() Method
Advertisements
 Previous Page Next Page  
Description
The method truncate() truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size.

The size defaults to the current position. The current file position is not changed. Note that if a specified size exceeds the file's current size, the result is platform-dependent.

Note − This method would not work in case file is opened in read-only mode.

Syntax
Following is the syntax for truncate() method −

fileObject.truncate( [ size ])
Parameters
size − If this optional argument is present, the file is truncated to (at most) that size.

Return Value
This method does not return any value.

Example
The following example shows the usage of truncate() method.

Assuming that 'foo.txt' file contains following text:
This is 1st line
This is 2nd line
This is 3rd line
This is 4th line
This is 5th line

"""

fo = open("References/02_T_Python3_Tutorialpoint/27_Files_Method/foo.txt", "r+")
print ("Name of the file: ", fo.name)

line = fo.readline()
print ("Read Line: %s" % (line))

fo.truncate()
line = fo.readlines()
print ("Read Line: %s" % (line))

# Close opened file
fo.close()

