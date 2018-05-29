

"""


Overriding Methods
You can always override your parent class methods. One reason for overriding parent's methods is that you may want special or different functionality in your subclass.


"""

class Parent:        # define parent class
   def myMethod(self):
      print ('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method


"""

When the above code is executed, it produces the following result −

Calling child method

"""
