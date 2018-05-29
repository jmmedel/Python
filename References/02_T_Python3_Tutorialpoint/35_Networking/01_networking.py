


"""

Python 3 - Network Programming

Python provides two levels of access to the network services. At a low level, you can access the basic socket support in the underlying operating system, which allows you to implement clients and servers for both connection-oriented and connectionless protocols.

Python also has libraries that provide higher-level access to specific application-level network protocols, such as FTP, HTTP, and so on.

This chapter gives you an understanding on the most famous concept in Networking - Socket Programming.

What is Sockets?
Sockets are the endpoints of a bidirectional communications channel. Sockets may communicate within a process, between processes on the same machine, or between processes on different continents.

Sockets may be implemented over a number of different channel types: Unix domain sockets, TCP, UDP, and so on. The socket library provides specific classes for handling the common transports as well as a generic interface for handling the rest.

Sockets have their own vocabulary −

S.No.	Term & Description
1	
domain

The family of protocols that is used as the transport mechanism. These values are constants such as AF_INET, PF_INET, PF_UNIX, PF_X25, and so on.

2	
type

The type of communications between the two endpoints, typically SOCK_STREAM for connection-oriented protocols and SOCK_DGRAM for connectionless protocols.

3	
protocol

Typically zero, this may be used to identify a variant of a protocol within a domain and type.

4	
hostname

The identifier of a network interface −

A string, which can be a host name, a dotted-quad address, or an IPV6 address in colon (and possibly dot) notation

A string "<broadcast>", which specifies an INADDR_BROADCAST address.

A zero-length string, which specifies INADDR_ANY, or

An Integer, interpreted as a binary address in host byte order.

5	
port

Each server listens for clients calling on one or more ports. A port may be a Fixnum port number, a string containing a port number, or the name of a service.

The socket Module
To create a socket, you must use the socket.socket() function available in the socket module, which has the general syntax −

s = socket.socket (socket_family, socket_type, protocol = 0)
Here is the description of the parameters −

socket_family − This is either AF_UNIX or AF_INET, as explained earlier.

socket_type − This is either SOCK_STREAM or SOCK_DGRAM.

protocol − This is usually left out, defaulting to 0.

Once you have socket object, then you can use the required functions to create your client or server program. Following is the list of functions required −

Server Socket Methods
S.No.	Method & Description
1	
s.bind()

This method binds address (hostname, port number pair) to socket.

2	
s.listen()

This method sets up and start TCP listener.

3	
s.accept()

This passively accept TCP client connection, waiting until connection arrives (blocking).

Client Socket Methods
S.No.	Method & Description
1	
s.connect()

This method actively initiates TCP server connection.

General Socket Methods
S.No.	Method & Description
1	
s.recv()

This method receives TCP message

2	
s.send()

This method transmits TCP message

3	
s.recvfrom()

This method receives UDP message

4	
s.sendto()

This method transmits UDP message

5	
s.close()

This method closes socket

6	
socket.gethostname()

Returns the hostname.

A Simple Server
To write Internet servers, we use the socket function available in socket module to create a socket object. A socket object is then used to call other functions to setup a socket server.

Now call the bind(hostname, port) function to specify a port for your service on the given host.

Next, call the accept method of the returned object. This method waits until a client connects to the port you specified, and then returns a connection object that represents the connection to that client.

"""
