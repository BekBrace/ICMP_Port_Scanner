''' Source ==== ICMP ECHO Request ===== > Destination 
    Source <==== ICMP ECHO Response ===== Destination '''
# Ping Sweeping
# Ping Scanning

import os
import platform

from datetime import datetime


# Selecting the range of IP address to ping sweep
net = input('Enter network address: ')
n1 = net.split('.')
a = '.'
n2 = n1[0] + a + n1[1] + a + n1[2] + a
alpha = int(input('Enter the first number >>> '))
omega = int(input('Enter the last number >>> '))
omega += 1
operation = platform.system()

# Selecting the command for ping sweeping based on OS
if (operation == "Windows"):
    ping1 = "ping -n 1"
elif (operation == "Linux"):
    ping1 = "ping -c 1"
else:
    ping1 = "ping -c 1"

t1 = datetime.now()

print('Scanning in progress ...')
# Giving a response about the host and time taken for completing the scanning
for ip in range(alpha, omega):
    addr = n2 + str(ip)
    comm = ping1 + addr
    res = os.popen(comm)

    for line in res.readlines():
        if(line.count("TTL")):
            break
        if (line.count("TTL")):
            print(addr, "--> LIVE!")
t2 = datetime.now()
total = t2-t1
print('Scanning completed in : ', total)
