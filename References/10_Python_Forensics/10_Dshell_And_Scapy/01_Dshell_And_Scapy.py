


"""

Python Forensics - Dshell and Scapy
DShell
Dshell is a Python-based network forensic analysis toolkit. This toolkit was developed by the US Army Research Laboratory. The release of this open source toolkit was in the year 2014. The major focus of this toolkit is to make forensic investigations with ease.

The toolkit consists of large number of decoders which are listed in the following table.

Sr.No.	Decoder Name & Description
1	
dns

This is used to extract DNS related queries

2	
reservedips

Identifies the solutions for DNS problems

3	
large-flows

Listing of the netflows

4	
rip-http

It is used extract the files from the HTTP traffic

5	
Protocols

Used for identification of non-standard protocols

The US Army Laboratory has maintained the clone repository in GitHub in the following link −

https://github.com/USArmyResearchLab/Dshell

Clone Repository
The clone consists of a script install-ubuntu.py () used for installation of this toolkit.

Once the installation is successful, it will automatically build the executables and dependencies that will be used later.

The dependencies are as follows −

dependencies = { 
   "Crypto": "crypto", 
   "dpkt": "dpkt", 
   "IPy": "ipy", 
   "pcap": "pypcap" 
}
This toolkit can be used against the pcap (packet capture) files, which is usually recorded during the incidents or during the alert. These pcap files is either created by libpcap on Linux platform or WinPcap on Windows platform.

Scapy
Scapy is a Python-based tool used to analyze and manipulate the network traffic. Following is the link for Scapy toolkit −

http://www.secdev.org/projects/scapy/

This toolkit is used to analyze packet manipulation. It is very capable to decode packets of a wide number of protocols and capture them. Scapy differs from the Dshell toolkit by providing a detailed description to the investigator about network traffic. These descriptions have been recorded in real time.

Scapy has the ability to plot using third-party tools or OS fingerprinting.

Consider the following example.



"""


import scapy, GeoIP #Imports scapy and GeoIP toolkit 
from scapy import * 
geoIp = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE) #locates the Geo IP address 
def locatePackage(pkg): 
    src = pkg.getlayer(IP).src #gets source IP address 
    dst = pkg.getlayer(IP).dst #gets destination IP address 
    srcCountry = geoIp.country_code_by_addr(src) #gets Country details of source 
    dstCountry = geoIp.country_code_by_addr(dst) #gets country details of destination 
print (src+"("+srcCountry+") >> "+dst+"("+dstCountry+")\n")
