

"""
Python 3 - Nested loops
Python programming language allows the usage of one loop inside another loop. The following section shows a few examples to illustrate the concept.

Syntax
for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
The syntax for a nested while loop statement in Python programming language is as follows −

while expression:
   while expression:
      statement(s)
   statement(s)
A final note on loop nesting is that you can put any type of loop inside any other type of loop. For example a for loop can be inside a while loop or vice versa.

Example
The following program uses a nested-for loop to display multiplication tables from 1-10."""

import sys
for i in range(1,11):
   for j in range(1,11):
      k=i*j
      print (k , end=' ')
   print()

"""
The print() function inner loop has end=' ' which appends a space instead of default newline. Hence, the numbers will appear in one row.

Last print() will be executed at the end of inner for loop."""

