


"""

he server accepting the request for communication channel will include the following script.


"""


# server.py
import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name 
host = socket.gethostname()
port = 8080

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests 
serversocket.listen(5)

while True:
   # establish a connection 
   clientsocket,addr = serversocket.accept()
   print("Got a connection from %s" % str(addr))
   currentTime = time.ctime(time.time()) + "\r\n"
   clientsocket.send(currentTime.encode('ascii'))
   clientsocket.close()

"""

The client and server created with the help of Python programming listen to the host number. Initially, the client sends a request to the server with respect to data sent in the host number and the server accepts the request and sends a response immediately. This way, we can have a secure channel of communication.


"""
