import os
import sys
import argparse
import socket
import scapy
import requests
#import threading
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore,Style

#phantom logo
logo = ( Fore.BLUE + r"""
*----------*-----------*----------*---------*---------*---------*-----------*----------*
            ____  _   _ __  __     __  __ _____ _   _ _    _
           |  _ \| | | |  \/  |   |  \/  | ____| \ | | |  | |
           | |_) | |_| | |\/| |   | |\/| |  _| |  \| | |  | |
           |  __/|  _  | |  | |   | |  | | |___| |\  | |__| |
           |_|   |_| |_|_|  |_|   |_|  |_|_____|_| \_|\_____/
*--------*-----------*-----------*----------*-----------*--------*-----------*----------*
""" +Style.RESET_ALL )

#arguments
parser = argparse.ArgumentParser(description="Phantom~network~Scanner")

parser.add_argument("-t" , "--target" ,type=str ,required=True, help="target IP or Domain")
parser.add_argument("-p" , "--port",type=int , help="port number to scan")

#scan range
parser.add_argument('-pS', action='store_true', help='Common port scan')
parser.add_argument('-pC', action='store_true', help='Custom port scan')
parser.add_argument('-pA', action='store_true', help='All ports scan')

#scan types 
#parser.add_argument('-sP', action='store_true', help='Ping scan')
parser.add_argument('-sS', action='store_true', help='SYN scan')
parser.add_argument('-sA', action='store_true', help='ACK scan')
parser.add_argument('-sT', action='store_true', help='TCP three way handshake full')
parser.add_argument('-sU', action='store_true', help='UDP scan')
parser.add_argument('-sF', action='store_true', help='FIN scan')
parser.add_argument('-sX', action='store_true', help='Xmas scan')
parser.add_argument('-sN', action='store_true', help='Null scan')


args = parser.parse_args()

#Port Scanner
common_services = {
    20: "FTP Data",21: "FTP Control",22: "SSH",23: "Telnet",25: "SMTP",53: "DNS",67: "DHCP Server",68: "DHCP Client",
    69: "TFTP",80: "HTTP",110: "POP3",123: "NTP",135: "RPC",137: "NetBIOS Name",138: "NetBIOS Datagram",
    139: "NetBIOS Session",143: "IMAP",161: "SNMP",162: "SNMP Trap",389: "LDAP",443: "HTTPS",445: "SMB",
    465: "SMTP (SSL)",514: "Syslog",587: "SMTP (TLS)",636: "LDAP (SSL)",993: "IMAPS",995: "POP3S",
    1433: "MS SQL Server",1521: "Oracle Database",1723: "PPTP VPN",3306: "MySQL",3389: "RDP",5900: "VNC",
    8080: "HTTP Proxy",8443: "HTTPS Proxy",9200: "Elasticsearch",27017: "MongoDB"
}

target = args.target
ports = list(common_services.keys())

def common_port_scan(target ,ports):
#   service = common_services.get(port)
    print(Fore.BLUE + f"[*] Target: {target}")
    print(Fore.BLUE + f"Scanning for common ports...")


    if not (args.sT or args.sU):
        print(Fore.RED + "[*] No scan type selected, defaulting to TCP scan (-sT) \n")
        args.sT = True
    # TCP scan ...
    if args.sT:
        print(Fore.BLUE + "[&] TCP  scan...\n")
        try:
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target,port))

                if result == 0:
                        banner = sock.recv(1024).decode().strip()
                        print(Fore.GREEN + f"[+] {port}  Banner : {banner} : OPEN")
                sock.close()

        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Scan interrupted by user.")
            sys.exit(0)
        except socket.gaierror:
            print(Fore.RED +"\n[!] Hostname could not be resolved.")
            sys.exit(0)
        except socket.error:
            print(Fore.RED +"\n[!] Couldn't connect to server.")
            sys.exit(0)

#UDP scan ...
'''   elif args.sU:
        print(Fore.BLUE + "[&] UDP scan...\n")
        try:
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(1)
                sock.sendto(b'', (target, port))
                try:
                    data, addr = sock.recvfrom(1024)
                    print(Fore.GREEN + f"[+] {port}  {service} : OPEN (Responded)")
                except socket.timeout:
                    print(Fore.RED + f"[-] {port} {service} : OPEN|FILTERED (No response)")
                finally:
                    sock.close()
        except Exception as e:
            print(Fore.RED + f"[-] {port} : CLOSED|FILTERED")
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Scan interrupted by user.")
            sys.exit(0)
        except socket.gaierror:
            print(Fore.RED +"\n[!] Hostname could not be resolved.")
            sys.exit(0)
        except socket.error:
            print(Fore.RED +"\n[!] Couldn't connect to server.")
            sys.exit(0)
        '''
if __name__ == "__main__":

    os.system('clear' if os.name == 'posix' else 'cls')
    print(logo,"\n \n")
    print(Fore.BLUE + "[*] Phantom Network Scanner \n")
# Default to common port scan if no type is selected
    if not (args.pS or args.pC or args.pA):
        print(Fore.RED + "[!] No port type selected , default to common port scan (-pS)")
        args.pS = True
    if args.pS:
        common_port_scan(target,ports)

