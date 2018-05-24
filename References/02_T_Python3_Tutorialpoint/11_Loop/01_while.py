


"""
Python while Loop Statements
A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true.

Syntax
The syntax of a while loop in Python programming language is −

while expression:
   statement(s)
Here, statement(s) may be a single statement or a block of statements. The condition may be any expression, and true is any non-zero value. The loop iterates while the condition is true.

When the condition becomes false, program control passes to the line immediately following the loop.

In Python, all the statements indented by the same number of character spaces after a programming construct are considered to be part of a single block of code. Python uses indentation as its method of grouping statements."""

"""
Here, key point of the while loop is that the loop might not ever run. When the condition is tested and the result is false, the loop body will be skipped and the first statement after the while loop will be executed."""

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")

"""
The block here, consisting of the print and increment statements, is executed repeatedly until count is no longer less than 9. With each iteration, the current value of the index count is displayed and then increased by 1."""



