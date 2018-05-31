


"""


Python - Tuples
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

Creating a tuple is as simple as putting different comma-separated values. Optionally you can put these comma-separated values between parentheses also. For example −

The empty tuple is written as two parentheses containing nothing −

tup1 = ();
To write a tuple containing a single value you have to include a comma, even though there is only one value −

tup1 = (50,);
Like string indices, tuple indices start at 0, and they can be sliced, concatenated, and so on.

Accessing Values in Tuples
To access values in tuple, use the square brackets for slicing along with the index or indices to obtain value available at that index. For example −

"""

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])


"""

When the above code is executed, it produces the following result −

tup1[0]:  physics
tup2[1:5]:  [2, 3, 4, 5]


"""


