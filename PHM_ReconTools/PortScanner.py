import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import scapy
import requests
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

def port_scan_runner(target,scan_type,scan_range):
    pass

# Ports scanning Range
def common_ports():
    pass

def all_ports():
    pass

def custom_ports():
    pass

#Port scanning methods or Types

def tcp_scan():
    pass    

def udp_scan():
    pass     

def syn_scan():
    pass

def fin_scan():
    pass    

def xmas_scan():
    pass

def null_scan():
    pass    

