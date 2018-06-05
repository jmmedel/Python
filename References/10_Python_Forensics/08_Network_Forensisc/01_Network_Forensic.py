


"""

Python Forensics - Network Forensics

The scenario of modern network environments is such that investigating can be fraught due to a number of difficulties. This can happen whether you are responding to a breach support, investigating insider activities, performing assessments related to vulnerability, or validating a regulatory compliance.

Concept of Network Programming
The following definitions are used in network programming.

Client − Client is a part of client-server architecture of network programming which runs on a personal computer and workstation.

Server − The server is a part of client-server architecture that provides services to other computer programs in the same or other computers.

WebSockets − WebSockets provide a protocol between the client and the server, which runs over a persistent TCP connection. Through this, bi-directional messages can be sent between the TCP socket connection (simultaneously).

WebSockets come after many other technologies that allow the servers to send information to the client. Other than handshaking the Upgrade Header, WebSockets is independent from HTTP.

Network Programming
These protocols are used to validate the information which is sent or received by the third party users. As encryption is one of the methods used for securing messages, it is also important to secure the channel through which the messages have been transferred.

Consider the following Python program, which the client uses for handshaking.

Example


"""

# client.py
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 8080

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
tm = s.recv(1024)
print("The client is waiting for connection")
s.close()

