


"""


Python - Advanced Linked list


We have already seen Linked List in earlier chapter in whihc it is possible only to travle forward. In this chapter we see another type of linked list in which it is possible to travle both forward and backward. Such a linked list is called Doubly Linked List. Following is the features of doubly linked list.

    Doubly Linked List contains a link element called first and last.
    Each link carries a data field(s) and two link fields called next and prev.
    Each link is linked with its next link using its next link.
    Each link is linked with its previous link using its previous link.
    The last link carries a link as null to mark the end of the list.

Creating Doubly linked list

We create a Doubly Linked list by using the Node class. Now we use the same approach as used in the Singly Linked List but the head and next pointers will be used for proper assignation to create two links in each of the nodes in addition to the data present in the node.

"""


class Node:
       def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class doubly_linked_list:

   def __init__(self):
      self.head = None

# Adding data elements		
   def push(self, NewVal):
      NewNode = Node(NewVal)
      NewNode.next = self.head
      if self.head is not None:
         self.head.prev = NewNode
      self.head = NewNode

# Print the Doubly Linked list		
   def listprint(self, node):
      while (node is not None):
         print(node.data),
         last = node
         node = node.next

dllist = doubly_linked_list()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.listprint(dllist.head)


"""

When the above code is executed, it produces the following result −

62 8 12



"""
