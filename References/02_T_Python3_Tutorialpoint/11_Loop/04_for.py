

"""
Python 3 - for Loop Statements
The for statement in Python has the ability to iterate over the items of any sequence, such as a list or a string.

Syntax
for iterating_var in sequence:
   statements(s)
If a sequence contains an expression list, it is evaluated first. Then, the first item in the sequence is assigned to the iterating variable iterating_var. Next, the statements block is executed. Each item in the list is assigned to iterating_var, and the statement(s) block is executed until the entire sequence is exhausted."""

"""
The range() function
The built-in function range() is the right function to iterate over a sequence of numbers. It generates an iterator of arithmetic progressions.

Example
Example
range() generates an iterator to progress integers starting with 0 upto n-1. To obtain a list object of the sequence, it is typecasted to list(). Now this list can be iterated using the for statement."""
list(range(5))
for var in list(range(5)):
    print(var)
print()

for letter in "Python":
    print("Current Letter :",letter)
print()

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)

print ("Good bye!")