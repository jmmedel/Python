


"""

Adding a column
We can add column to a matrix using the insert() method. here we have to mention the index where we want to add the column and a array containing the new values of the columns added. In the below example we add t a new column at the fifth position from the begining.


"""

from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)

print(m_c)


"""

When the above code is executed, it produces the following result −


[['Mon' '18' '20' '22' '17' '1']
 ['Tue' '11' '18' '21' '18' '2']
 ['Wed' '15' '21' '20' '19' '3']
 ['Thu' '11' '20' '22' '21' '4']
 ['Fri' '18' '17' '23' '22' '5']
 ['Sat' '12' '22' '20' '18' '6']
 ['Sun' '13' '15' '19' '16' '7']]
 

"""



