


"""

Accessing Values in a Matrix
The data elements in a matrix can be accessed by using the indexes. The access methos is same as the way data is accessed in Two dimensional array.



"""

from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
# Print data for Wednesday
print(m[2])

# Print data for friday evening
print(m[4][3])


"""

When the above code is executed, it produces the following result −

['Wed', 15, 21, 20, 19]
23

"""

