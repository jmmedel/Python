

"""

Python 3 - File next() Method

Description
File object in Python 3 doesn't support next() method. Python 3 has a built-in function next() which retrieves the next item from the iterator by calling its __next__() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised. This method can be used to read the next input line, from the file object

Syntax
Following is the syntax for next() method −

next(iterator[,default])
Parameters
iterator − file object from which lines are to be read

default − returned if iterator exhausted. If not given, StopIteration is raised

Return Value
This method returns the next input line.

Example
The following example shows the usage of next() method.

"""


# Open a file
fo = open("References/02_T_Python3_Tutorialpoint/27_Files_Method/foo.txt", "r")
print ("Name of the file: ", fo.name)

for index in range(5):
   line = next(fo)
   print ("Line No %d - %s" % (index, line))

# Close opened file
fo.close()



