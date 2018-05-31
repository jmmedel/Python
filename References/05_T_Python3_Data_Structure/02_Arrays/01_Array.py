


"""

Python - Arrays

rray is a container which can hold a fix number of items and these items should be of the same type. Most of the data structures make use of arrays to implement their algorithms. Following are the important terms to understand the concept of Array.

Element− Each item stored in an array is called an element.
Index − Each location of an element in an array has a numerical index, which is used to identify the element.
Array Representation
Arrays can be declared in various ways in different languages. Below is an illustration.

Array DeclarationArray Representation
As per the above illustration, following are the important points to be considered.

Index starts with 0.

Array length is 10 which means it can store 10 elements.

Each element can be accessed via its index. For example, we can fetch an element at index 6 as 9.

Basic Operations
Following are the basic operations supported by an array.

Traverse − print all the array elements one by one.

Insertion − Adds an element at the given index.

Deletion − Deletes an element at the given index.

Search − Searches an element using the given index or by the value.

Update − Updates an element at the given index.

Array is created in Python by importing array module to the python program. Then the array is declared as shown eblow.


from array import *

arrayName = array(typecode, [Initializers])
Typecode are the codes that are used to define the type of value the array will hold. Some common typecodes used are:

Typecode	Value
b	Represents signed integer of size 1 byte/td>
B	Represents unsigned integer of size 1 byte
c	Represents character of size 1 byte
i	Represents signed integer of size 2 bytes
I	Represents unsigned integer of size 2 bytes
f	Represents floating point of size 4 bytes
d	Represents floating point of size 8 bytes
Before lookign at various array operations lets create and print an array using python.

The below code creates an array named array1.


"""

from array import *

array1 = array('i', [10,20,30,40,50])

for x in array1:
 print(x)
 

