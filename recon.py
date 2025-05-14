import os
import sys
import argparse
import socket
import scapy
import requests
import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore,Style
from datetime import datetime
#
#date and time management
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%Y-%m-%d")
#
#
#arguments
parser = argparse.ArgumentParser(description="Phantom~network~Scanner")
#
parser.add_argument("-t" , "--target" ,type=str ,required=True, help="target IP or Domain")
parser.add_argument("-p" , "--port",type=int , help="port number to scan")
#
#scan range
parser.add_argument('-pS', action='store_true', help='Common port scan')
parser.add_argument('-pC', action='store_true', help='Custom port scan')
parser.add_argument('-pA', action='store_true', help='All ports scan')
#
#scan types 
#parser.add_argument('-sP', action='store_true', help='Ping scan')
parser.add_argument('-sS', action='store_true', help='SYN scan')
parser.add_argument('-sA', action='store_true', help='ACK scan')
parser.add_argument('-sT', action='store_true', help='TCP three way handshake full')
parser.add_argument('-sU', action='store_true', help='UDP scan')
parser.add_argument('-sF', action='store_true', help='FIN scan')
parser.add_argument('-sX', action='store_true', help='Xmas scan')
parser.add_argument('-sN', action='store_true', help='Null scan')
#
#whois lookup flag
parser.add_argument('-wh', action='store_true', help='whois lookup')
# Subdomain enumeration and Directory scanner
parser.add_argument('-sub', action='store_true', help='Subdomain enumeration')
parser.add_argument('-dir', action='store_true', help='Directory scanner')
#
args = parser.parse_args()
#
#Port Scanner
common_services = {
    20: "FTP Data",21: "FTP Control",22: "SSH",23: "Telnet",25: "SMTP",53: "DNS",67: "DHCP Server",68: "DHCP Client",
    69: "TFTP",80: "HTTP",110: "POP3",123: "NTP",135: "RPC",137: "NetBIOS Name",138: "NetBIOS Datagram",
    139: "NetBIOS Session",143: "IMAP",161: "SNMP",162: "SNMP Trap",389: "LDAP",443: "HTTPS",445: "SMB",
    465: "SMTP (SSL)",514: "Syslog",587: "SMTP (TLS)",636: "LDAP (SSL)",993: "IMAPS",995: "POP3S",
    1433: "MS SQL Server",1521: "Oracle Database",1723: "PPTP VPN",3306: "MySQL",3389: "RDP",5900: "VNC",
    8080: "HTTP Proxy",8443: "HTTPS Proxy",9200: "Elasticsearch",27017: "MongoDB"
}

whois_servers = {
    ".com": "whois.verisign-grs.com",
    ".net": "whois.verisign-grs.com",
    ".org": "whois.pir.org",
    ".in": "whois.registry.in",
    ".co.in": "whois.registry.in",
    ".edu.in": "whois.registry.in",
    ".gov.in": "whois.registry.in",
    ".io": "whois.nic.io",
    ".me": "whois.nic.me"
}
#
target = args.target
ports = list(common_services.keys())
#
#if you want to modify it , kindly only use functions , no use of classes or any OOP thingy ...
#OOP will increase my task and slowen the project growth ...
#And also i am not a fan of OOP ... so please no OOP in this project ...
#And use comments , so make it more understandable , i might forgot half of comments so its all to you to understand it ...
#

###########################################################################################################
#scan methods


# three way handshake (TCP)
def three_way_handshake(target, port):

        #scan for common ports
        if args.pS:
            port_openorfiltered = []           
            try:
                for port in ports:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((target,port))

                    if result == 0:
                        try:
                            banner = sock.recv(1024).decode(errors="ignore").strip()
                            port_openorfiltered.append(Fore.LIGHTWHITE_EX + f"[+] {port} Banner: {banner}  |OPEN" +Style.RESET_ALL)
                            #print(Fore.LIGHTWHITE_EX + f"[+] {port} Banner: {banner}  |OPEN" +Style.RESET_ALL )
                            
                        except socket.error:
                            port_openorfiltered.append(Fore.LIGHTWHITE_EX + f"[+] {port} No Banner |OPEN" +Style.RESET_ALL )
                            #print(Fore.LIGHTWHITE_EX + f"[+] {port} No Banner |OPEN" +Style.RESET_ALL )      
                    sock.close()
                time.sleep(0.5)
                print(port_openorfiltered,"\n")
            except KeyboardInterrupt:
                print(Fore.RED + "\n[!] Scan interrupted by user."  +Style.RESET_ALL )
                sys.exit(0)
            except socket.gaierror:
                print(Fore.RED +"\n[!] Hostname could not be resolved."  +Style.RESET_ALL )
                sys.exit(0)
            except socket.error as e:
                print(Fore.RED +"\n[!] Couldn't connect to server.",  +Style.RESET_ALL )
                sys.exit(0)
        #scan for all ports
        if args.pA:
            pass
        #scan for custom ports
        if args.pC:
            pass


def syn_scan(target, port):
    pass

def ack_scan(target, port):
    pass

def fin_scan(target, port):
    pass

def xmas_scan(target, port):
    pass

def null_scan(target, port):
    pass

def UDP_scan(target, port):
    #UDP scan ...
    # elif args.sU:
    #     print(Fore.BLUE + "[&] UDP scan...\n")
    #     try:
    #         for port in ports:
    #             sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #             sock.settimeout(1)
    #             sock.sendto(b'', (target, port))
    #             try:
    #                 data, addr = sock.recvfrom(1024)
    #                 print(Fore.GREEN + f"[+] {port}  {service} : OPEN (Responded)")
    #             except socket.timeout:
    #                 print(Fore.RED + f"[-] {port} {service} : OPEN|FILTERED (No response)")
    #             finally:
    #                 sock.close()
    #     except Exception as e:
    #         print(Fore.RED + f"[-] {port} : CLOSED|FILTERED")
    #     except KeyboardInterrupt:
    #         print(Fore.RED + "\n[!] Scan interrupted by user.")
    #         sys.exit(0)
    #     except socket.gaierror:
    #         print(Fore.RED +"\n[!] Hostname could not be resolved.")
    #         sys.exit(0)
    #     except socket.error:
    #         print(Fore.RED +"\n[!] Couldn't connect to server.")
    #         sys.exit(0)
    pass


#########################################################################################################
#Scan types
def common_port_scan():
#scan method chooser
    if args.sT:
     print(args.sT)
     print(Fore.LIGHTBLACK_EX + "[&] TCP Three Way Handshake scan...\n"  +Style.RESET_ALL )
    #  with ThreadPoolExecutor(max_workers=10) as executor:
    #     for port in ports:
    #         executor.submit(three_way_handshake, target, port)
     port_results = []
    
     try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
            # Create a dictionary mapping futures to ports
            future_to_port = {
                executor.submit(three_way_handshake, target, port): port for port in ports
            }
            
            # Process completed futures as they complete
            for future in concurrent.futures.as_completed(future_to_port):
                try:
                    port, is_open, banner = future.result()
                    if is_open:
                        if banner:
                            port_results.append(
                                Fore.LIGHTWHITE_EX + f"[+] {port} Banner: {banner} |OPEN" + Style.RESET_ALL
                            )
                        else:
                            port_results.append(
                                Fore.LIGHTWHITE_EX + f"[+] {port} No Banner |OPEN" + Style.RESET_ALL
                            )
                except Exception as exc:
                    pass
                    # port = future_to_port[future]
                    # print(f"Port {port} generated an exception: {exc}")
     except KeyboardInterrupt:
         pass
#     three_way_handshake(target, ports)
    elif args.sS:
        pass
    elif args.sU:
        UDP_scan(target, ports)
    elif args.sA:
        pass
    elif args.sF:
        pass
    elif args.sX:
        pass
    elif args.sN:
        pass
    else:
        pass


#this is a function for whois loopup , flag = -wh
def extract_tld(target):
    parts = target.lower().split('.')
    if len(parts) >= 3:
        sub_tld = "." + parts[-2] + "." + parts[-1]  # e.g., .edu.in
        if sub_tld in whois_servers:
            return sub_tld
    if len(parts) >= 2:
        tld = "." + parts[-1]  # e.g., .com
        if tld in whois_servers:
            return tld
    return None

def whois_lookup(target):
    tld = extract_tld(target)
    if not tld:
        return Fore.RED + f"[-] Unsupported or unknown TLD for domain '{target}'."+  Style.RESET_ALL
    server = whois_servers[tld]
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server, 43))
            s.sendall((target + "\r\n").encode())
            response = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                response += data
        return response.decode(errors="ignore")
    except Exception as e:
        return f"[!] Error connecting to WHOIS server: {e}"

def whois_main(target):
    print(Fore.GREEN + f"[+] Performing WHOIS lookup for: {target}")
    result = whois_lookup(target)
    print(Fore.GREEN + f"{result}")
#######################################################################################################

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

    print(Fore.LIGHTBLACK_EX+ f"Target: {args.target}  |  Mode: {scan_type}  |  Ports: {scan_range}"+Style.RESET_ALL)

#port scanning functions
    if args.pS:
        common_port_scan()

#other functons
    if args.wh:
        whois_main(target)
    if args.sub:
        pass    
    if args.dir:
        pass

    print(Fore.LIGHTBLACK_EX + "\n[!] Recon completed."  +Style.RESET_ALL )
    print(Fore.LIGHTBLACK_EX + "[!] Exiting..."  +Style.RESET_ALL )
    sys.exit(0)