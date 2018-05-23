"""
Python 3 - Number round() Method
Description
round() is a built-in function in Python. It returns x rounded to n digits from the decimal point.
Syntax
Following is the syntax for the round() method −

round( x [, n]  )
Parameters
x − This is a numeric expression.

n − Represents number of digits from decimal point up to which x is to be rounded. Default is 0.

Return Value
This method returns x rounded to n digits from the decimal point.

Example
The following example shows the usage of round() method."""

print ("round(70.23456) : ", round(70.23456))
print ("round(56.659,1) : ", round(56.659,1))
print ("round(80.264, 2) : ", round(80.264, 2))
print ("round(100.000056, 3) : ", round(100.000056, 3))
print ("round(-100.000056, 3) : ", round(-100.000056, 3))
