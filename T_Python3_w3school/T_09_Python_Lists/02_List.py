


""" 

The list() Constructor
It is also possible to use the list() constructor to make a list. To add an item to the list use append() object method. To remove a specific item use the remove() object method. The len() function returns the length of the list.

"""

# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Using the append() method to append an item:

thislist = list(("apple", "banana", "cherry"))
thislist.append("damson")

print(thislist)

#Using the remove() method to remove an item:

thislist = list(("apple", "banana", "cherry"))
thislist.remove("banana")

print(thislist)


# The len() method returns the number of items in a list:
thislist = list(("apple", "banana", "cherry"))
print(len(thislist))