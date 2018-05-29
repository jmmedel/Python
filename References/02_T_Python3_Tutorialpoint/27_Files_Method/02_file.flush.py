


"""

Python 3 - File flush() Method
Advertisements
 Previous Page Next Page  
Description
The method flush() flushes the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects.

Python automatically flushes the files when closing them. But you may want to flush the data before closing any file.

Syntax
Following is the syntax for flush() method −

fileObject.flush()
Parameters
NA

Return Value
This method does not return any value.

Example
The following example shows the usage of flush() method.


"""

# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)

# Here it does nothing, but you can call it with read operation.
fo.flush()

# Close opend file
fo.close()


