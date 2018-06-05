


"""

Replacing in a Heap
The heapreplace function always removes the smallest element of the heap and inserts the new incoming element at some place not fixed by any order.



"""

import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)


