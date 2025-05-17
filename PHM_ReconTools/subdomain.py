import requests
import os
from colorama import Fore, Style
#from concurrent.futures import ThreadPoolExecutor, as_completed

def check_subdomain(domain, subdomain_list):
    print(Fore.LIGHTBLACK_EX + f"[*] Starting Subdomain Enumeration for {domain}...")
    active_subdomains = []
    for sub in subdomain_list:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code < 400:
                found_url = Fore.LIGHTWHITE_EX + f"[+] Found: {url}" + Style.RESET_ALL
#                print(Fore.LIGHTWHITE_EX + f"[+] Found: {url}")
                active_subdomains.append(url)
        except requests.ConnectionError:
            pass
  
    return active_subdomains

def run_subdomain(domain): 
    try:
    
        with open("PHM_ReconTools\wordlists\subdomain.txt", "r") as file:
            subdomains = [line.strip() for line in file]
        found_subdomains = check_subdomain(domain, subdomains)
        for sub in found_subdomains:
            print(Fore.LIGHTWHITE_EX + f"{sub} \n")
        print(Fore.LIGHTBLACK_EX +"|Subdomain Scan Completed| \n" + Style.RESET_ALL)
        print("=="*50, "\n")

    except FileNotFoundError:
        print(Fore.RED + "[!] Subdomain file not found. Please ensure 'subdomain.txt' exists in the 'PHM_ReconTools\wordlists\' directory.")