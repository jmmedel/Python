

"""
The set() Constructor
It is also possible to use the set() constructor to make a set. You can use the add() object method to add an item, and the remove() object method to remove an item from the set. The len() function returns the size of the set."""

# Using the set() Constructor  to make a set:

thisset = set(("apple","Banana","Cherry")) # note the double round brackets
print(thisset)

#using the add() method to add an item:

thisset = set(("Apple","banna","Cherry"))
thisset.add("Damson")
print(thisset)

#Usng the remove() method to remote an item'

thisset = set(("Apple","Banna","Cherry"))
thisset.remove ("Banna")
print(thisset)