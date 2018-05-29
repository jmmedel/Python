


"""

Python 3 - File seek() Method
Advertisements
 Previous Page Next Page  
Description
The method seek() sets the file's current position at the offset. The whence argument is optional and defaults to 0, which means absolute file positioning, other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end.

There is no return value. Note that if the file is opened for appending using either 'a' or 'a+', any seek() operations will be undone at the next write.

If the file is only opened for writing in append mode using 'a', this method is essentially a no-op, but it remains useful for files opened in append mode with reading enabled (mode 'a+').

If the file is opened in text mode using 't', only offsets returned by tell() are legal. Use of other offsets causes undefined behavior.

Note that not all file objects are seekable.

Syntax
Following is the syntax for seek() method −

fileObject.seek(offset[, whence])
Parameters
offset − This is the position of the read/write pointer within the file.

whence − This is optional and defaults to 0 which means absolute file positioning, other values are 1 which means seek relative to the current position and 2 means seek relative to the file's end.

Return Value
This method does not return any value.

Example
The following example shows the usage of seek() method.

Assuming that 'foo.txt' file contains following text:
This is 1st line
This is 2nd line
This is 3rd line
This is 4th line
This is 5th line


"""

# Open a file
fo = open("References/02_T_Python3_Tutorialpoint/27_Files_Method/foo.txt", "r+")
print ("Name of the file: ", fo.name)

line = fo.readlines()
print ("Read Line: %s" % (line))

# Again set the pointer to the beginning
fo.seek(0, 0)
line = fo.readline()
print ("Read Line: %s" % (line))

# Close opened file
fo.close()

