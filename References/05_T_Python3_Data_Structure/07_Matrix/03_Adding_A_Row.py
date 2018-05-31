


"""

Adding a row

"""

from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m_r = append(m,[['Avg',12,15,13,11]],0)

print(m_r)



"""

When the above code is executed, it produces the following result −


[['Mon' '18' '20' '22' '17']
 ['Tue' '11' '18' '21' '18']
 ['Wed' '15' '21' '20' '19']
 ['Thu' '11' '20' '22' '21']
 ['Fri' '18' '17' '23' '22']
 ['Sat' '12' '22' '20' '18']
 ['Sun' '13' '15' '19' '16']
 ['Avg' '12' '15' '13' '11']]

"""





