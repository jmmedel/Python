


"""

Traversing the Node Elements

We can traverse the elements of the node created above by creating a variable and assigning the first element to it. Then we use a while loop and nextval pointer to print out all the node elements. Note that we have one more additional data element and the nextval pointers are properly arranged to get the output as a days of a week in a proper sequence.



"""


class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Wed')
e3 = daynames('Tue')
e4 = daynames('Thu')

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

thisvalue = e1

while thisvalue:
        print(thisvalue.dataval)
        thisvalue = thisvalue.nextval


"""

When the above code is executed, it produces the following result.

Mon
Tue
Wed
Thu

The additional operations like insertion and deletion can be done by implementing appropriate methods by using this node containers in the general data structures like linked lists and trees. So we study them in the next chapters.


"""



