


"""

The read() Method
The read() method reads a string from an open file. It is important to note that Python strings can have binary data. apart from text data.

Syntax
fileObject.read([count]);
Here, passed parameter is the number of bytes to be read from the opened file. This method starts reading from the beginning of the file and if count is missing, then it tries to read as much as possible, maybe until the end of file.

Example
Let us take a file foo.txt, which we created above.


"""


# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

# Close opened file
fo.close()
