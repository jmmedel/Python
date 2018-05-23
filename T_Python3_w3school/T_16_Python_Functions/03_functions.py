

"""
Lambda Functions
In python, the keyword lambda is used to create what is known as anonymous functions. These are essentially functions with no pre-defined name. They are good for constructing adaptable functions, and thus good for event handling.

Example
An anonymous function that returns the double value of i:"""

myfunc = lambda i: i*2
print(myfunc(2))

"""
Lambda defined functions can have more than one defined input, as shown here:"""

myfunc = lambda x,y: x*y
print(myfunc(3,6))

"""
The power of lambda is better shown when you generate anonymous functions at run-time, as shown in the following example."""


def myfunc2(n):
  return lambda i: i*n

doubler = myfunc2(2)
tripler = myfunc2(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))


"""
Here we see the defined function, myfunc, which creates an anonymous function that doubles some on-the-fly variable i with a just-in-time variable n representing our multiplier.

We then create two variables doubler and tripler, which are assigned to the result of myfunc passing in 2 and 3 respectively. They are assigned to the generated lambda functions."""
