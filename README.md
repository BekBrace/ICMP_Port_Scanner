# ICMP_Port_Scanner
This is a port Scanner using ICMP Technic [ Educational Purpose Only - Never use this for illegal actions ] 

# ICMP_Port_Scanner
This is a port Scanner using ICMP Technic [ Educational Purpose Only - Never use this for illegal actions ] 

Port Scanner using ICMP (Live hosts in a network)

Internet Control Message Protocol (ICMP) which is a supporting protocol in the ip suite. 

It is used by network devices, including routers, to send error messages and  information indicating success or failure when communicating with another IP address.


ICMP is not a port scan but it is used to ping the remote host to check if the host is up. 
This scan is useful when we have to check a number of live hosts in a network. 
It involves sending an ICMP ECHO Request to a host and if that host is live, it will return an ICMP ECHO Reply.

 Source ==== ICMP ECHO Request ===== > Destination 
Source <==== ICMP ECHO Response ===== Destination 

And the ICMP Request through Ping sweeping and not ping scanning
And what it is, just a process to find more than one machine availability in a specific network range.
Ping scanning is very time consuming if we want to check a range of IP addresses for example, as it will do it one by one sequentially.
