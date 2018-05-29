


"""

Python 3 - File tell() Method
Advertisements
 Previous Page Next Page  
Description
The method tell() returns the current position of the file read/write pointer within the file.

Syntax
Following is the syntax for tell() method −

fileObject.tell()
Parameters
NA

Return Value
This method returns the current position of the file read/write pointer within the file.

Example
The following example shows the usage of tell() method.

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

pos=fo.tell()
print ("current position : ",pos)

# Close opened file
fo.close()


