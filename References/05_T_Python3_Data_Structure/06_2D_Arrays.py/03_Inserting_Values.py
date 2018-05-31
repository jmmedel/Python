

"""

Inserting Values in Two Dimensional Array
We can insert new data elements at specific position by using the insert() method and specifying the index.

In the below example a new data element is inserted at index position 2.


"""

from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T.insert(2, [0,5,11,13,6])

for r in T:
    for c in r:
        print(c,end = " ")
    print()
    


