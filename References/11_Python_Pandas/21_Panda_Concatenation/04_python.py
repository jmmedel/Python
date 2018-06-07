

import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print (pd.concat([one,two],axis=1))



"""


Its output is as follows −

    Marks_scored    Name  subject_id   Marks_scored    Name   subject_id
1           98      Alex      sub1         89         Billy         sub2
2           90       Amy      sub2         80         Brian         sub4
3           87     Allen      sub4         79          Bran         sub3
4           69     Alice      sub6         97         Bryce         sub6
5           78    Ayoung      sub5         88         Betty         sub5

"""



