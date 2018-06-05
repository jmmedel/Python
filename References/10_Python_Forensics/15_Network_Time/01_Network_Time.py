


"""

Python Forensics - Network Time Protocol

The most widely used protocol for synchronizing time and which has been widely accepted as a practice is done through Network Time Protocol (NTP).

NTP uses the User Datagram Protocol (UDP) which uses minimum time to communicate the packets between the server and the client who wish to synchronize with the given time source.

Network Time Protocol
Features of Network Time Protocol are as follows −

The default server port is 123.

This protocol consists of many accessible time servers synchronized to national laboratories.

The NTP protocol standard is governed by the IETF and the Proposed Standard is RFC 5905, titled “Network Time Protocol Version 4: Protocol and Algorithms Specification” [NTP RFC]

Operating systems, programs, and applications use NTP to synchronize time in a proper way.

In this chapter, we will focus on the usage of NTP with Python, which is feasible from third-party Python Library ntplib. This library efficiently handles the heavy lifting, which compares the results to my local system clock.

Installing the NTP Library
The ntplib is available for download at https://pypi.python.org/pypi/ntplib/ as shown in the following figure.

The library provides a simple interface to NTP servers with the help of methods that can translate NTP protocol fields. This helps access other key values such as leap seconds.

Installing the NTP Library
The following Python program helps in understanding the usage of NTP.



"""

import ntplib
import time

NIST = 'nist1-macon.macon.ga.us'
ntp = ntplib.NTPClient()
ntpResponse = ntp.request(NIST)

if (ntpResponse):
   now = time.time()
   diff = now-ntpResponse.tx_time
   print diff;
   


