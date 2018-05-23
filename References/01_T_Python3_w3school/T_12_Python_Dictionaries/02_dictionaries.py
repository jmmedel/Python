

"""
The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary:"""

thisdict =	dict(apple="green", banana="yellow", cherry="red")
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

"""
Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:"""

thisdict =	dict(apple="green", banana="yellow", cherry="red")
thisdict["damson"] = "purple"
print(thisdict)

"""
Removing Items
Removing a dictionary item must be done using the del() function in python:"""

thisdict =	dict(apple="green", banana="yellow", cherry="red")
del(thisdict["banana"])
print(thisdict)

"""
Get the Length of a Dictionary
The len() function returns the size of the dictionary:"""

thisdict =	dict(apple="green", banana="yellow", cherry="red")
print(len(thisdict))

