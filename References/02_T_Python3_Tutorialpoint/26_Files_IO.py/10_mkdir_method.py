

"""


Directories in Python
All files are contained within various directories, and Python has no problem handling these too. The os module has several methods that help you create, remove, and change directories.

The mkdir() Method
You can use the mkdir() method of the os module to create directories in the current directory. You need to supply an argument to this method, which contains the name of the directory to be created.

Syntax
os.mkdir("newdir")
Example
Following is an example to create a directory test in the current directory −

"""


import os

# Create a directory "test"
os.mkdir("test")


