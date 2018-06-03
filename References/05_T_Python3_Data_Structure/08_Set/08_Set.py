


"""



Compare Sets

We can check if a given set is a subset or superset of another set. The result is True or False depending on the elements present in the sets.

"""


DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)


"""

When the above code is executed, it produces the following result.

True
True

"""


