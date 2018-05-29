


"""


Renaming and Deleting Files
Python os module provides methods that help you perform file-processing operations, such as renaming and deleting files.

To use this module, you need to import it first and then you can call any related functions.

The rename() Method
The rename() method takes two arguments, the current filename and the new filename.

Syntax
os.rename(current_file_name, new_file_name)
Example
Following is an example to rename an existing file test1.txt 


"""


import os

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )


