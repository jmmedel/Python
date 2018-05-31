


"""

Updating Values in Two Dimensional Array
We can update the entire inner array or some specific data elements of the inner array by reassigning the values using the array index.


"""


from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T[2] = [11,9]
T[0][3] = 7
for r in T:
    for c in r:
        print(c,end = " ")
    print()


"""

When the above code is executed, it produces the following result −

11 12 5 7 
15 6 10 
11 9 
12 15 8 6

"""


