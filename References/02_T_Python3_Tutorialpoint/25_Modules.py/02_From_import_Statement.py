

"""


The from...import Statement
Python's from statement lets you import specific attributes from a module into the current namespace. The from...import has the following syntax −

from modname import name1[, name2[, ... nameN]]
For example, to import the function fibonacci from the module fib, use the following statement −"""





from fib import fib
print(fib(100))


"""

This statement does not import the entire module fib into the current namespace; it just introduces the item fibonacci from the module fib into the global symbol table of the importing module.

"""
