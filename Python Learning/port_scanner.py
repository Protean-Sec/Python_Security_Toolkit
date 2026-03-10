import socket
import sys
from datetime import datetime
socket.setdefaulttimeout(0.5)
open_ports = []
def scan(targets, ports,):
    for port in range(4440, ports):
        scan_port(targets, port)




def scan_port(ip_address, port,):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_address, port))
        open_ports.append(port)
        print("Port is open " + str(port))
        sock.close()
    except:
        pass

targets = input("Enter target to scan: (split by comma) ")
ports = int(input("Enter amount of ports to scan: "))
if "," in targets:
    print("Scanning...")
    for ip_address in targets.split(","):
        scan(ip_address.strip(), ports)
else:
    scan(targets, ports)


print("Port Scanning Completed! Port opened is: "+ str(open_ports))
print("Time accessed  " + str(datetime.now()))
sys.exit(0)
