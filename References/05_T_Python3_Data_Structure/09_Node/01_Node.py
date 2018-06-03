

"""

Python - Nodes

here are situations when the allocation of memory to store the data cannot be in a continuous block of memory. So we take help of pointers where the along with the data, the address of the next location of data element is also stored. So we know the address of the next data element from the values of current data element. In general such structures are known as pointers. But in Python we refer them as Nodes.

Nodes are the foundations on which various other data structures linked lists and tress can be handled in python.
Creation of Nodes

The nodes are created by implementing a class which will hold the pointers along with the data element. In the below example we create a class named daynames to hold the name of the weekdays. The nextval pointer is initialized to null and three nodes and initialized with values as shown.

The nextval pointer of node e1 poimts to e3 while the nextval pointer of node e3 points to e2.


"""


class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Tue')
e3 = daynames('Wed')

e1.nextval = e3
e3.nextval = e2


"""



"""

