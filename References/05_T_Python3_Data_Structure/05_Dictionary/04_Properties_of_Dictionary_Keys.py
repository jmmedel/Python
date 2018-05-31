


"""

Properties of Dictionary Keys
Dictionary values have no restrictions. They can be any arbitrary Python object, either standard objects or user-defined objects. However, same is not true for the keys.

There are two important points to remember about dictionary keys −

(a) More than one entry per key not allowed. Which means no duplicate key is allowed. When duplicate keys encountered during assignment, the last assignment wins. For example −



"""

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict['Name']: ", dict['Name'])

"""

When the above code is executed, it produces the following result −

dict['Name']:  Manni

"""


"""

(b) Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed. Following is a simple example −


"""

dict = {['Name']: 'Zara', 'Age': 7}
print ("dict['Name']: ", dict['Name'])

"""

When the above code is executed, it produces the following result −

Traceback (most recent call last):
   File "test.py", line 3, in <module>
      dict = {['Name']: 'Zara', 'Age': 7};
TypeError: list objects are unhashable"""







