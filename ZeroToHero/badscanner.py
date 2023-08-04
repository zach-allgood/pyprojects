#!/bin/python3

import sys
import socket
from datetime import datetime

#Define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 badscanner.py <ip>")

#Banner
print("-" * 50)
print(f"Scanning target {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname {target} could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to the server.")
    sys.exit()