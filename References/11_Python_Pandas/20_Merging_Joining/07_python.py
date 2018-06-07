


"""


Inner Join
Joining will be performed on index. Join operation honors the object on which it is called. So, a.join(b) is not equal to b.join(a).

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
print (pd.merge(left, right, on='subject_id', how='inner'))

"""

Its output is as follows −

    Name_x   id_x   subject_id   Name_y   id_y
0      Amy      2         sub2    Billy      1
1    Allen      3         sub4    Brian      2
2    Alice      4         sub6    Bryce      4
3   Ayoung      5         sub5    Betty      5



"""

