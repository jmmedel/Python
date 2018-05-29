


"""

Python 3 - File writelines() Method
Advertisements
 Previous Page Next Page  
Description
The method writelines() writes a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings. There is no return value.

Syntax
Following is the syntax for writelines() method −

fileObject.writelines( sequence )
Parameters
sequence − This is the Sequence of the strings.

Return Value
This method does not return any value.

Example
The following example shows the usage of writelines() method.

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

seq = ["This is 6th line\n", "This is 7th line"]
# Write sequence of lines at the end of the file.
fo.seek(0, 2)
line = fo.writelines( seq )

# Now read complete file from beginning.
fo.seek(0,0)
   for index in range(7):
      line = next(fo)
      print ("Line No %d - %s" % (index, line))

# Close opened file
fo.close()

