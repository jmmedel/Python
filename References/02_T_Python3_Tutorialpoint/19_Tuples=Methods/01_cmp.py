
"""
Python 3 - Tuple cmp() Method
Description
The cmp() method compares elements of two tuples.

Syntax
Following is the syntax for cmp() method −

cmp(tuple1, tuple2)
Parameters
tuple1 − This is the first tuple to be compared

tuple2 − This is the second tuple to be compared

Return Value
If elements are of the same type, perform the compare and return the result. If elements are different types, check to see if they are numbers.

If numbers, perform numeric coercion if necessary and compare.

If either element is a number, then the other element is "larger" (numbers are "smallest").

Otherwise, types are sorted alphabetically by name.

If we reached the end of one of the tuples, the longer tuple is "larger." If we exhaust both tuples and share the same data, the result is a tie, meaning that 0 is returned.

Example
The following example shows the usage of cmp() method."""


tuple1, tuple2 = (123, 'xyz'), (456, 'abc')

print cmp(tuple1, tuple2)
print cmp(tuple2, tuple1)
tuple3 = tuple2 + (786,)
print cmp(tuple2, tuple3)
