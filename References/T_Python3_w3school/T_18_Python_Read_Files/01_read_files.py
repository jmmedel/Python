

"""
Python File Open
Open a File on the Server
Asume we have the following file, located in the same folder as Python:"""

"""
To open the file, use the built-in open() function.

The open() function returns a file object, which has a read() method for reading the content of the file:"""

f = open("demofile.txt", "r")
print(f.read())


