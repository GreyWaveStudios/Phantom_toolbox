import os
import sys
import argparse
import socket
import scapy
import requests
import time
#import threading
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore,Style
from datetime import datetime

#date and time management
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%Y-%m-%d")


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

    # TCP scan ...
    if args.sT:
        print(Fore.LIGHTWHITE_EX + "[&] TCP  scan...\n"  +Style.RESET_ALL )
        try:
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target,port))

                if result == 0:
                        try:
                            banner = sock.recv(1024).decode(errors="ignore").strip()
                            print(Fore.LIGHTBLACK_EX + f"[+] {port} ,Banner: {banner}  |OPEN" +Style.RESET_ALL )
                        except socket.error:
                            print(Fore.LIGHTBLACK_EX + f"[+] {port} , No Banner |OPEN" +Style.RESET_ALL )
                        
                sock.close()
                time.sleep(0.5)

        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Scan interrupted by user."  +Style.RESET_ALL )
            sys.exit(0)
        except socket.gaierror:
            print(Fore.RED +"\n[!] Hostname could not be resolved."  +Style.RESET_ALL )
            sys.exit(0)
        except socket.error as e:
            print(Fore.RED +"\n[!] Couldn't connect to server.",  +Style.RESET_ALL )
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
    print(Fore.BLUE+ f"Phantom Recon v0.1.1 | By Phantom Group"+Style.RESET_ALL)
    print(Fore.BLUE+ f"Starting Recon at Date: {current_date} | Time: {current_time}"+Style.RESET_ALL)
#target | Mode | Ports
    if args.pS:
        scan_type = "Common"
    elif args.pC:       
        scan_type = "Custom"
    elif args.pA:
        scan_type = "All"
    elif not (args.pS or args.pC or args.pA):
        scan_type = "Common"
        args.pS = True
    else:
        print(Fore.LIGHTBLACK_EX + "Invalid Port Range"  +Style.RESET_ALL )

    if args.sT:
        scan_range = "TCP"
    elif args.sU:     
        scan_range = "UDP"
    elif args.sF:
        scan_range = "FIN"
    elif args.sX:
        scan_range = "Xmas"
    elif args.sN:
        scan_range = "Null"
    elif args.sA:
        scan_range = "ACK"
    elif args.sS:
        scan_range = "SYN"
    elif not (args.sT or args.sU or args.sF or args.sX or args.sN or args.sA or args.sS):
        scan_range = "TCP"
        args.sT = True
    else:
        print(Fore.LIGHTBLACK_EX + "Invalid Scan Type"  +Style.RESET_ALL )

    print(Fore.LIGHTWHITE_EX+ f"Target: {args.target}  |  Mode: {scan_type}  |  Ports: {scan_range}"+Style.RESET_ALL)

    if args.pS:
        common_port_scan(target,ports)

