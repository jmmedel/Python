

"""

Python 3 - File fileno() Method
Advertisements
 Previous Page Next Page  
Description
The method fileno() returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system.

Syntax
Following is the syntax for fileno() method −

fileObject.fileno() 
Parameters
NA

Return Value
This method returns the integer file descriptor.

Example
The following example shows the usage of fileno() method.


"""

# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)

fid = fo.fileno()
print ("File Descriptor: ", fid)

# Close opend file
fo.close()



