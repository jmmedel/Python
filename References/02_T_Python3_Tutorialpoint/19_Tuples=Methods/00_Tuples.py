


"""
Basic Tuples Operations
Tuples respond to the + and * operators much like strings; they mean concatenation and repetition here too, except that the result is a new tuple, not a string.

In fact, tuples respond to all of the general sequence operations we used on strings in the previous chapter.

Python Expression	Results	Description
len((1, 2, 3))	3	Length
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	Concatenation
('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	Repetition
3 in (1, 2, 3)	True	Membership
for x in (1,2,3) : print (x, end = ' ')	1 2 3	Iteration
Indexing, Slicing, and Matrixes
Since tuples are sequences, indexing and slicing work the same way for tuples as they do for strings, assuming the following input −

T=('C++', 'Java', 'Python')
Python Expression	Results	Description
T[2]	'Python'	Offsets start at zero
T[-2]	'Java'	Negative: count from the right
T[1:]	('Java', 'Python')	Slicing fetches sections
No Enclosing Delimiters
No enclosing Delimiters is any set of multiple objects, comma-separated, written without identifying symbols, i.e., brackets for lists, parentheses for tuples, etc., default to tuples, as indicated in these short examples.

Built-in Tuple Functions
Python includes the following tuple functions −

S.No.	Function & Description
1	cmp(tuple1, tuple2)
Compares elements of both tuples.

2	len(tuple)
Gives the total length of the tuple.

3	max(tuple)
Returns item from the tuple with max value.

4	min(tuple)
Returns item from the tuple with min value.

5	tuple(seq)
Converts a list into tuple."""
