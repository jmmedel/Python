


"""


Update a row in in a Matrix
To update the values in the row of a matrix we simply re-assign the values at the index of the row. In the below example all the values for thrursday's data is marked as zero. The index for this row is 3.


"""


from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m[3] = ['Thu',0,0,0,0]

print(m)


"""

When the above code is executed, it produces the following result −

[['Mon' '18' '20' '22' '17']
 ['Tue' '11' '18' '21' '18']
 ['Wed' '15' '21' '20' '19']
 ['Thu' '0' '0' '0' '0']
 ['Fri' '18' '17' '23' '22']
 ['Sat' '12' '22' '20' '18']
 ['Sun' '13' '15' '19' '16']]



"""
