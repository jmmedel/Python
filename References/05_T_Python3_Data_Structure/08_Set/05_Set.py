


"""

Union of Sets

The union operation on two sets produces a new set containing all the distinct elements from both the sets. In the below example the element “Wed” is present in both the sets.


"""

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)


"""

When the above code is executed, it produces the following result. Please note the result has only one “wed”.

set(['Wed', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat'])


"""


