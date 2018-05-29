



"""



"""


#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
msg = s.recv(1024)                                     

s.close()
print (msg.decode('ascii'))


"""
Now run this server.py in the background and then run the above client.py to see the result.

# Following would start a server in background.
$ python server.py & 

# Once server is started run client as follows:
$ python client.py
Output
This would produce following result −

on server terminal
Got a connection from ('192.168.1.10', 3747)
On client terminal
Thank you for connecting


"""
