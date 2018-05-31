


"""

Python - 2D Array
Two dimensional array is an array within an array. It is an array of arrays. In this type of array the position of an data element is referred by two indices instead of one. So it represents a table with rows an dcolumns of data. In the below example of a twp dimensional array, observer that each array element itself is also an array.

Consider the example of recording temperatures 4 times a day, every day. Some times the recording instrument may be faulty and we fail to record data. Such data for 4 days can be presented as a two dimensional array as below.

Day 1 - 11 12 5 2 
Day 2 - 15 6 10 
Day 3 - 10 8 12 5 
Day 4 - 12 15 8 6 
The above data can be represented as a two dimensional array as below.

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

"""


"""

Accessing Values in a Two Dimensional Array
The data elements in two dimesnional arrays can be accessed using two indices. One index referring to the main or parent array and another index referring to the position of the data element in the inner array. If we mention only one index then the entire inner array is printed for that index position. The example below illustrates how it works.


"""


from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

print(T[0])

print(T[1][2])

"""

When the above code is executed, it produces the following result −

[11, 12, 5, 2]
10


"""


