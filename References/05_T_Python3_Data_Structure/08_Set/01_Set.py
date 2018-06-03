


"""

Python - Sets
 Mathematically a set is a collection of items not in any particular order. A Python set is similar to this mathematical definition with below additional conditions.

    The elements in the set cannot be duplicates.
    The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.
    There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

Set Operations

The sets in python are typically used for mathematical operations like union, intersection, difference and complement etc. We can create a set, access it’s elements and carry out these mathematical operations as shown below.
Creating a set

A set is created by using the set() function or placing all the elements within a pair of curly braces.


"""


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)
 

"""

When the above code is executed, it produces the following result. Please note how the order of the elements has changed in the result.

 
set(['Wed', 'Sun', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat'])
set(['Jan', 'Mar', 'Feb'])
set([17, 21, 22])
 
 

"""





