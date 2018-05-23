

""" 
Python Tuples
 Tuple
A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets. """

# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Return the item in position 1:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#You cannot change values in a tuple:
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant" # test changeability
print(thistuple)


