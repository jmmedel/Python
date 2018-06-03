

"""

Python - Deque

A double-ended queue, or deque, has the feature of adding and removing elements from either end. The Deque module is a part of collections library. It has the methods for adding and removing elements which can be invoked directly with arguments. In the below program we import the collections module and declare a deque. Without need of any class we use the in-built implement these methods directly.


"""

import collections
# Create a deque
DoubleEnded = collections.deque(["Mon","Tue","Wed"])
print (DoubleEnded)

# Append to the right
print("Adding to the right: ")
DoubleEnded.append("Thu")
print (DoubleEnded)

# append to the left
print("Adding to the left: ")
DoubleEnded.appendleft("Sun")
print (DoubleEnded)

# Remove from the right
print("Removing from the right: ")
DoubleEnded.pop()
print (DoubleEnded)

# Remove from the left
print("Removing from the left: ")
DoubleEnded.popleft()
print (DoubleEnded)

# Reverse the dequeue
print("Reversing the deque: ")
DoubleEnded.reverse()
print (DoubleEnded)


"""


When the above code is executed, it produces the following result:

deque(['Mon', 'Tue', 'Wed'])
Adding to the right: 
deque(['Mon', 'Tue', 'Wed', 'Thu'])
Adding to the left: 
deque(['Sun', 'Mon', 'Tue', 'Wed', 'Thu'])
Removing from the right: 
deque(['Sun', 'Mon', 'Tue', 'Wed'])
Removing from the left: 
deque(['Mon', 'Tue', 'Wed'])
Reversing the deque: 
deque(['Wed', 'Tue', 'Mon'])

"""
