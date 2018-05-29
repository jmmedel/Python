


"""

User-Defined Exceptions
Python also allows you to create your own exceptions by deriving classes from the standard built-in exceptions.

Here is an example related to RuntimeError. Here, a class is created that is subclassed from RuntimeError. This is useful when you need to display more specific information when an exception is caught.

In the try block, the user-defined exception is raised and caught in the except block. The variable e is used to create an instance of the class Networkerror.


class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
So once you have defined the above class, you can raise the exception as follows −

try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args
   
"""
