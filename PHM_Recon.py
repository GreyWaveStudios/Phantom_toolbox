from PHM_ReconTools import *
import argparse
import os
import sys
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from colorama import Fore,Style
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%Y-%m-%d")

#arguments
parser = argparse.ArgumentParser(description="Phantom~network~Scanner")
parser.add_argument("-td" , "--target" ,type=str ,required=True, help="target Domain")
parser.add_argument("-p" , "--port",type = str, help="port number to scan")
parser.add_argument('-pS', action='store_true', help='Common port scan')
parser.add_argument('-pC', action='store_true', help='Custom port scan')
parser.add_argument('-pA', action='store_true', help='All ports scan')
parser.add_argument('-sP', action='store_true', help='Ping host activity scan')
parser.add_argument('-sS', action='store_true', help='SYN scan')
parser.add_argument('-sA', action='store_true', help='ACK scan')
parser.add_argument('-sT', action='store_true', help='TCP three way handshake full')
parser.add_argument('-sU', action='store_true', help='UDP scan')
parser.add_argument('-sF', action='store_true', help='FIN scan')
parser.add_argument('-sX', action='store_true', help='Xmas scan')
parser.add_argument('-sN', action='store_true', help='Null scan')
parser.add_argument('-wh', action='store_true', help='whois lookup')
parser.add_argument('-sub', action='store_true', help='Subdomain enumeration')
parser.add_argument('-dir', action='store_true', help='Directory scanner')
args = parser.parse_args()


target = args.target
port_range = args.port

#start_port, end_port = map(int, port_range.split('-'))

if __name__ == "__main__":
    print(Fore.BLUE+ f"Phantom Recon v0.1.5 | By [Phantom Group]"+Style.RESET_ALL)
    print(Fore.BLUE+ f"Starting Recon at Date: {current_date} | Time: {current_time}"+Style.RESET_ALL)


    if args.pS:
        PortScanner.common_ports(target,args=args)
    elif args.pA:
        PortScanner.all_ports(target,args=args)
    elif args.pC:
        PortScanner.custom_ports(target,args=args)

    if args.sub:
        subdomain.run_subdomain(target)

    if args.wh:
        whois.whois_main(target)


    print(Fore.BLUE+ f"Recon completed at Date: {current_date} | Time: {current_time}"+Style.RESET_ALL)
    sys.exit(0)