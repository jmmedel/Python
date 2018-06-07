


"""


Merge Using 'how' Argument
The how argument to merge specifies how to determine which keys are to be included in the resulting table. If a key combination does not appear in either the left or the right tables, the values in the joined table will be NA.

Here is a summary of the how options and their SQL equivalent names −

Merge Method	SQL Equivalent	Description
left	LEFT OUTER JOIN	Use keys from left object
right	RIGHT OUTER JOIN	Use keys from right object
outer	FULL OUTER JOIN	Use union of keys
inner	INNER JOIN	Use intersection of keys

Left Join

"""


import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print (pd.merge(left, right, on='subject_id', how='left'))


"""

Its output is as follows −

    Name_x   id_x   subject_id   Name_y   id_y
0     Alex      1         sub1      NaN    NaN
1      Amy      2         sub2    Billy    1.0
2    Allen      3         sub4    Brian    2.0
3    Alice      4         sub6    Bryce    4.0
4   Ayoung      5         sub5    Betty    5.0


"""


