

"""


Insertion Operation
Insert operation is to insert one or more data elements into an array. Based on the requirement, a new element can be added at the beginning, end, or any given index of array.

Here, we add a data element at the middle of the array using the python in-built insert() method.


"""


from array import *

array1 = array('i', [10,20,30,40,50])

array1.insert(1,60)

for x in array1:
 print(x)



"""

When we compile and execute the above program, it produces the following result which shows the element is inserted at index position 1.

Output

10
60
20
30
40
50


"""
