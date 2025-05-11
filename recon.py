import os
import sys
import argparse
import socket
import requests
#import threading
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore

#arguments
parser = argparse.ArgumentParser(description="Phantom~network~Scanner")

parser.add_argument("-t" , "--target" ,type=str ,required=True, help="target IP or Domain")
parser.add_argument("-p" , "--port",type=int , help="port number to scan")
parser.add_argument('-sS', action='store_true', help='TCP SYN scan (common)')
parser.add_argument('-sC', action='store_true', help='Custom port scan')
parser.add_argument('-sA', action='store_true', help='All ports scan')
parser.add_argument('-pT', action='store_true', help='TCP protocol')
parser.add_argument('-pU', action='store_true', help='UDP protocol')

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
'''
def common_port_scan(target , port):
    print(Fore.BLUE + f"Scanning for common ports...\n")
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket_type )
            socket.settimeout(1)
            result = sock.connect_ex((target,port))
            if socket_type == socket.SOCK_STREAM :
                if result == 0:
                    service = common_services.get(port)
                    print(Fore.GREEN + f"[+] {port}  {service} : OPEN")
            sock.close()
            if socket_type == socket.SOCK_DGRAM:

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

def common_port_scan(target ,ports):
    print(Fore.BLUE + f"Scanning for common ports...\n")
    # TCP scan ...
    if args.pT:
        try:
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target,port))
                if result == 0:
                        service = common_services.get(port)
                        print(Fore.GREEN + f"[+] {port}  {service} : OPEN")
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
    elif args.pU:
        try:
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(1)
                sock.sendto(b'', (target, port))
        except Exception as e:
            print(e)
