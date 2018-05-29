


"""

Variable-length Arguments
You may need to process a function for more arguments than you specified while defining the function. These arguments are called variable-length arguments and are not named in the function definition, unlike required and default arguments.

Syntax for a function with non-keyword variable arguments is given below −

def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]
An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments. This tuple remains empty if no additional arguments are specified during the function call. Following is a simple example −



"""

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
      print(arg1, "This is arg1")
   return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )


