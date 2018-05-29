

"""

The from...import * Statement
It is also possible to import all the names from a module into the current namespace by using the following import statement −

from modname import *
This provides an easy way to import all the items from a module into the current namespace; however, this statement should be used sparingly.

Executing Modules as Scripts
Within a module, the module’s name (as a string) is available as the value of the global variable __name__. The code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__".

Add this code at the end of your module −


"""


# Fibonacci numbers module

def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result
if __name__ == "__main__":
   f = fib(100)
   print(f)
   
