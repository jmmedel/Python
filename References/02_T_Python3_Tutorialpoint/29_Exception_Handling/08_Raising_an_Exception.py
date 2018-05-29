


"""

Raising an Exception
You can raise exceptions in several ways by using the raise statement. The general syntax for the raise statement is as follows −

Syntax
raise [Exception [, args [, traceback]]]
Here, Exception is the type of exception (for example, NameError) and argument is a value for the exception argument. The argument is optional; if not supplied, the exception argument is None.

The final argument, traceback, is also optional (and rarely used in practice), and if present, is the traceback object used for the exception.

Example
An exception can be a string, a class or an object. Most of the exceptions that the Python core raises are classes, with an argument that is an instance of the class. Defining new exceptions is quite easy and can be done as follows −


"""

def functionName( level ):
   if level <1:
      raise Exception(level)
      # The code below to this would not be executed
      # if we raise the exception
   return level

"""
Note − In order to catch an exception, an "except" clause must refer to the same exception thrown either as a class object or a simple string. For example, to capture the above exception, we must write the except clause as follows −

try:
   Business Logic here...
except Exception as e:
   Exception handling here using e.args...
else:
   Rest of the code here...
   
"""

