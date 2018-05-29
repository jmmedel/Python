
"""
Python 3 - Date & Time
Advertisements
 Previous Page Next Page  
A Python program can handle date and time in several ways. Converting between date formats is a common chore for computers. Python's time and calendar modules help track dates and times.

What is Tick?
Time intervals are floating-point numbers in units of seconds. Particular instants in time are expressed in seconds since 12:00am, January 1, 1970(epoch).

There is a popular time module available in Python which provides functions for working with times, and for converting between representations. The function time.time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch).


"""

import time;  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

"""

This would produce a result something as follows −

Number of ticks since 12:00am, January 1, 1970: 1455508609.34375
Date arithmetic is easy to do with ticks. However, dates before the epoch cannot be represented in this form. Dates in the far future also cannot be represented this way - the cutoff point is sometime in 2038 for UNIX and Windows.

"""



