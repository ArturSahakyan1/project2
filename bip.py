import subprocess
import re
import time

def block_ip(ip_address):
    command = ["iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"]
    subprocess.run(command)

def unblock_ip(ip_address):
    command = ["iptables", "-D", "INPUT", "-s", ip_address, "-j", "DROP"]
    subprocess.run(command)

def main():
    failed_attempts = {}  # Dictionary to store failed attempts per IP

    while True:
        auth_log = subprocess.check_output(["grep", "sshd.*Failed", "/var/log/auth.log"], universal_newlines=True)
        lines = auth_log.strip().split('\n')

        for line in lines:
            match = re.search(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip_address = match.group(1)
                if ip_address in failed_attempts:
                    failed_attempts[ip_address] += 1
                else:
                    failed_attempts[ip_address] = 1

                if failed_attempts[ip_address] >= 3:
                    print(f"Blocking {ip_address} after 3 failed attempts")
                    block_ip(ip_address)
                    failed_attempts[ip_address] = 0
            else:
                match = re.search(r".*Accepted password for .* from (\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    ip_address = match.group(1)
                    if ip_address in failed_attempts:
                        print(f"Unblocking {ip_address} after successful login")
                        unblock_ip(ip_address)
                        failed_attempts[ip_address] = 0

        time.sleep(60)  # Check logs every 60 seconds

if __name__ == '__main__':
    main()

