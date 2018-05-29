


"""


Reading Keyboard Input
Python 2 has two built-in functions to read data from standard input, which by default comes from the keyboard. These functions are input() and raw_input()

In Python 3, raw_input() function is deprecated. Moreover, input() functions read data from keyboard as string, irrespective of whether it is enclosed with quotes ('' or "" ) or not.

The input Function
The input([prompt]) function is equivalent to raw_input, except that it assumes that the input is a valid Python expression and returns the evaluated result to you.


"""

x = input("Something")

print(x)

