

"""
The break Statement
With the break statement we can stop the loop before it has looped through all the items:

Example
Exit the loop when i is 3:"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


  """
  The continue Statement
With the continue statement we can stop the current iteration of the loop, and continue wit the next:

Example
Do not print banana:"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

