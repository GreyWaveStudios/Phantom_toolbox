import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import scapy
import requests
import sys
from colorama import Fore,Style

common_services = {
    20: "FTP Data",21: "FTP Control",22: "SSH",23: "Telnet",25: "SMTP",53: "DNS",67: "DHCP Server",68: "DHCP Client",
    69: "TFTP",80: "HTTP",110: "POP3",123: "NTP",135: "RPC",137: "NetBIOS Name",138: "NetBIOS Datagram",
    139: "NetBIOS Session",143: "IMAP",161: "SNMP",162: "SNMP Trap",389: "LDAP",443: "HTTPS",445: "SMB",
    465: "SMTP (SSL)",514: "Syslog",587: "SMTP (TLS)",636: "LDAP (SSL)",993: "IMAPS",995: "POP3S",
    1433: "MS SQL Server",1521: "Oracle Database",1723: "PPTP VPN",3306: "MySQL",3389: "RDP",5900: "VNC",
    8080: "HTTP Proxy",8443: "HTTPS Proxy",9200: "Elasticsearch",27017: "MongoDB"
}

all_port = 65535
ports = list(common_services.keys())
port_openorfiltered = []

def port_scan_runner(target,scan_type,scan_range):
    pass

# Ports scanning Range
def common_ports(domain,args):
    if args.sT:
        tcp_scan_S(domain)
        #print(port_openorfiltered)


def all_ports():
    pass

def custom_ports():
    pass

#Port scanning methods or Types

def tcp_scan_S(domain):
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((domain, port))

            if result == 0:
                        try:
                            banner = sock.recv(1024).decode(errors="ignore").strip()
                            print(Fore.LIGHTWHITE_EX + f"[+] {port}  |OPEN \n" +Style.RESET_ALL)
                            #port_openorfiltered.append(Fore.LIGHTWHITE_EX + f"[+] {port}  |OPEN \n" +Style.RESET_ALL)
                        except socket.error:
                            #port_openorfiltered.append(Fore.LIGHTWHITE_EX + f"[+] {port}  |OPEN \n" +Style.RESET_ALL )
                            print(Fore.LIGHTWHITE_EX + f"[+] {port}  |OPEN \n" +Style.RESET_ALL)
            sock.close()
    except KeyboardInterrupt:
                print(Fore.RED + "\n[!] Scan interrupted by user."  +Style.RESET_ALL )
                sys.exit(0)
    except socket.gaierror:
                print(Fore.RED +"\n[!] Hostname could not be resolved."  +Style.RESET_ALL )
                sys.exit(0)
    except socket.error as e:
                print(Fore.RED +"\n[!] Couldn't connect to server.",  +Style.RESET_ALL )
                sys.exit(0)


def udp_scan_S():
    pass     

def syn_scan_S():
    pass

def fin_scan_S():
    pass    

def xmas_scan_S():
    pass

def null_scan_S():
    pass    

