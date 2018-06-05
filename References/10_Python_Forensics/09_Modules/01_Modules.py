

"""

Python Forensics - Python Modules
Modules in Python programs help in organizing the code. They help in grouping related code into a single module, which makes it easier to understand and use. It includes arbitrarily named values, which can be used for binding and reference. In simple words, a module is a file consisting of Python code which includes functions, classes, and variables.

The Python code for a module (file) is saved with .py extension which is compiled as and when needed.

Example

def print_hello_func( par ): 
   print "Hello : ", par 
   return
Import Statement
The Python source file can be used as a module by executing an import statement which imports other packages or third-party libraries. The syntax used is as follows −

import module1[, module2[,... moduleN]
When the Python interpreter encounters the import statement, it imports the module specified which is present in the search path.

Example

Consider the following example.

#!/usr/bin/python

# Import module support
import support

# Now you can call defined function that module as follows
support.print_func("Radhika")
It will produce the following output −

Module Output
A module is loaded only once, regardless of the number of times it has been imported by Python code.

From...import statement
From attribute helps to import specific attributes from a module into a current namespace. Here is its syntax.

from modname import name1[, name2[, ... nameN]]
Example

To import the function fibonacci from the module fib, use the following statement.

from fib import fibonacci
Locating Modules
When the module is being imported, the Python interpreter searches for the following sequences −

The current directory.

If the module does not exist, Python then searches each directory in the shell variable PYTHONPATH.

If the shell variable location fails, Python checks the default path.

Computational forensics use Python modules and third-party modules to get the information and extract evidence with better ease. Further chapters focus on the implementation of modules to get the necessary output.

"""
