

"""
Default Parameter Value
The following example shows how to use a default paramter value.

If we call the function without parameter, it uses the default value:"""

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


"""
Return Values
To let a function return a value, use the return statement:

Example"""

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
