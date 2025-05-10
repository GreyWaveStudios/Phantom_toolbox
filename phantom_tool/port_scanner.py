import socket
import sys
import os
from colorama import Fore

common_services = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    135: "RPC",
    137: "NetBIOS Name",
    138: "NetBIOS Datagram",
    139: "NetBIOS Session",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTP (SSL)",
    514: "Syslog",
    587: "SMTP (TLS)",
    636: "LDAP (SSL)",
    993: "IMAPS",
    995: "POP3S",
    1433: "MS SQL Server",
    1521: "Oracle Database",
    1723: "PPTP VPN",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC",
    8080: "HTTP Proxy",
    8443: "HTTPS Proxy",
    9200: "Elasticsearch",
    27017: "MongoDB"
}

ports = list(common_services.keys())

def main_scanner(target, start_port, end_port):
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
        
            if result == 0:
                if port in ports:
                    com_port = common_services.get(port,"unknown")
                    print(Fore.GREEN + f"[+] port {port} for service {com_port} is OPEN")
                else:
                    print(Fore.GREEN + f"[+] Port {port} for 'unknown' service is OPEN")
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


def common_scan(target,ports):
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            com_port = common_services.get(port,"unknown")
            if result == 0:
                print(Fore.GREEN + f"[+] port {port} for service {com_port} is OPEN")
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

def port_scan():
    print(Fore.BLUE +"[1] Scan all ports \n[2] Scan common ports")
    scan_choice = input(Fore.BLUE +"[?] Choose the type of scan :")
    target = input(Fore.BLUE +"[*] Input target IP or domain :")
    
    if scan_choice == "1":
        if port_choice == "custom":
            port_choice = input(Fore.BLUE +"Press Enter to scan all ports (1-9999) or type 'custom' for a custom range: ").strip().lower()
            try:
                start_port = int(input(Fore.BLUE +"Enter start port: ").strip())
                end_port = int(input(Fore.BLUE +"Enter end port: ").strip())

                if start_port < 1 or end_port > 9999 or start_port > end_port:
                    print(Fore.RED +"[!] Invalid port range. Ports must be between 1-9999.")
                    sys.exit(0)
            except ValueError:
                print(Fore.RED +"[!] Invalid input. Please enter numbers only.")
                sys.exit(0)
        else:
            start_port, end_port = 1, 9999  # Default scan range


        main_scanner(target, start_port, end_port)
    elif scan_choice == "2":
        common_scan(target,ports)
