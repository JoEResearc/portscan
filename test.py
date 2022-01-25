import time
import os
import sys
from datetime import datetime
import pyfiglet
import socket

ascii_banner = pyfiglet.figlet_format("CrowdEye scanner")
print(ascii_banner)
print("Tools v1.0 By Joe | Research")
if len(sys.argv) == 2:

    target = socket.gethostbyname(sys.argv[1])
else:
    print("invalid amount of Argument")

print("-" * 50)
print("scanning target: " + target)
print("Scanning started at :" + str(datetime.now))
print("-" * 50)

try:

    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        resault = s.connect_ex((target,port))
        if resault ==0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program !!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved")
except socket.error:
    print("\n server not responding")
    sys.exit()
print("Done!!!!")