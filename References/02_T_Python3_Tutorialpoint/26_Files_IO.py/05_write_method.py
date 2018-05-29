


"""

Reading and Writing Files
The file object provides a set of access methods to make our lives easier. We would see how to use read() and write() methods to read and write files.

The write() Method
The write() method writes any string to an open file. It is important to note that Python strings can have binary data and not just text.

The write() method does not add a newline character ('\n') to the end of the string −

Syntax
fileObject.write(string);
Here, passed parameter is the content to be written into the opened file.

Example


"""

# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()


"""

The above method would create foo.txt file and would write given content in that file and finally it would close that file. If you would open this file, it would have the following content −

Python is a great language.
Yeah its great!!

"""


