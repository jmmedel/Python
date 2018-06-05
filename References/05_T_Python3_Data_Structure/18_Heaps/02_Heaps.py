


"""

Inserting into heap
Inserting a data element to a heap always adds the element at the last index. But you can apply heapify function again to bring the newly added element to the first index only if it smallest in value. In the below example we insert the number 8.



"""

import heapq
H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,8)
print(H)


"""

When the above code is executed, it produces the following result −

[1, 3, 5, 78, 21, 45]
[1, 3, 5, 78, 21, 45, 8]


"""


