


"""

Deletion Operation
Deletion refers to removing an existing element from the array and re-organizing all elements of an array.

Here, we remove a data element at the middle of the array using the python in-built remove() method.


"""

from array import *

array1 = array('i', [10,20,30,40,50])

array1.remove(40)

for x in array1:
 print(x)


"""

When we compile and execute the above program, it produces the following result which shows the element is removed form the array.

Output
10
20
30
50


"""

