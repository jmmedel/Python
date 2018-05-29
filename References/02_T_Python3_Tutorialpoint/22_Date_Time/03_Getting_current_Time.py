


"""

Getting current time
To translate a time instant from seconds since the epoch floating-point value into a timetuple, pass the floating-point value to a function (e.g., localtime) that returns a time-tuple with all valid nine items.

"""


import time

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

"""

This would produce the following result, which could be formatted in any other presentable form −

Local current time : time.struct_time(tm_year = 2016, tm_mon = 2, tm_mday = 15, 
   tm_hour = 9, tm_min = 29, tm_sec = 2, tm_wday = 0, tm_yday = 46, tm_isdst = 0)

"""

