import sys
import socket

def scan_ports(target, ports):
    open_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            open_ports.append(port)
        
        sock.close()

    return open_ports

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scan.py <target>")
        sys.exit(1)

    target = sys.argv[1]
    ports_to_scan = range(1, 65536)  # Scan all ports from 1 to 65535

    open_ports = scan_ports(target, ports_to_scan)

    if open_ports:
        print("Open ports on", target, ":", open_ports)
    else:
        print("No open ports found on", target)

