



"""


Delete a column from a Matrix
We can delete a column from a matrix using the delete() method. We have to specify the index of the column and also the axis value which is 0 for a row and 1 for a column.


"""

from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m = delete(m,s_[2],1)

print(m)


"""

When the above code is executed, it produces the following result −

[['Mon' '18' '22' '17']
 ['Tue' '11' '21' '18']
 ['Wed' '15' '20' '19']
 ['Thu' '11' '22' '21']
 ['Fri' '18' '23' '22']
 ['Sat' '12' '20' '18']
 ['Sun' '13' '19' '16']]
 

"""

