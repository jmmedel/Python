


"""

Deleting the Values in Two Dimensional Array
We can delete the entire inner array or some specific data elements of the inner array by reassigning the values using the del() method with index. But in case you need to remove specific data elements in one of the inner arrays, then use the update process described above.


"""

from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

del T[3]

for r in T:
    for c in r:
        print(c,end = " ")
    print()


"""

When the above code is executed, it produces the following result −

11 12 5 2 
15 6 10 
10 8 12 5 

"""
