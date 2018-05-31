


"""

Update Operation
Update operation refers to updating an existing element from the array at a given index.

Here, we simply reassign a new value to the desired index we want to update.



"""

from array import *

array1 = array('i', [10,20,30,40,50])

array1[2] = 80

for x in array1:
 print(x)


"""

When we compile and execute the above program, it produces the following result which shows the new value at the index position 2.

Output
10
20
80
40
50


"""



