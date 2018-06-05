


"""

Removing from heap
You can remove the element at first index by using this function. In the below example the function will always remove the element at the index position 1.

"""

import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Remove element from the heap
heapq.heappop(H)

print(H)

"""

When the above code is executed, it produces the following result −

[1, 3, 5, 78, 21, 45]
[3, 21, 5, 78, 45]

"""

