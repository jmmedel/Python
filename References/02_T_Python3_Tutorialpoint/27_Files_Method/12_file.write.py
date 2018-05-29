

"""

Python 3 - File write() Method
Advertisements
 Previous Page Next Page  
Description
The method write() writes a string str to the file. There is no return value. Due to buffering, the string may not actually show up in the file until the flush() or close() method is called.

Syntax
Following is the syntax for write() method −

fileObject.write( str )
Parameters
str − This is the String to be written in the file.

Return Value
This method does not return any value.

Example
The following example shows the usage of write() method.

Assuming that 'foo.txt' file contains following text:
This is 1st line
This is 2nd line
This is 3rd line
This is 4th line
This is 5th line

"""

# Open a file in read/write mode
fo = open("References/02_T_Python3_Tutorialpoint/27_Files_Method/foo.txt", "r+")
print ("Name of the file: ", fo.name)

str = "This is 6th line"
# Write a line at the end of the file.
fo.seek(0, 2)
line = fo.write( str )

# Now read complete file from beginning.
fo.seek(0,0)
   for index in range(6):
      line = next(fo)
      print ("Line No %d - %s" % (index, line))

# Close opened file
fo.close()

