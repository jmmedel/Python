

"""
Elif
The elif keyword is pythons way of saying "if the previous conditions were not true, then do this condition"."""


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

"""
In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal"."""

"""
Else
The else keyword catches anyting which isn't caught by the preceding conditions."""

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  """
  In this example a is greater to b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b"."""
  