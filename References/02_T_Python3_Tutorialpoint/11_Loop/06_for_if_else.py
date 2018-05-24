"""
Using else Statement with Loops
Python supports having an else statement associated with a loop statement.

If the else statement is used with a for loop, the else block is executed only if for loops terminates normally (and not by encountering break statement).

If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

Example
The following example illustrates the combination of an else statement with a for statement that searches for even number in given list."""

numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list doesnot contain even number')
