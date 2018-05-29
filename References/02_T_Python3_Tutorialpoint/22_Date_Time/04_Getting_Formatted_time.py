


"""

Getting formatted time
You can format any time as per your requirement, but a simple method to get time in a readable format is asctime() −


"""


import time

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

