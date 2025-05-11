'''import requests
import os
from colorama import Fore


# Function to check subdomain
def check_subdomain(domain, subdomain_list):
    os.system('clear' if os.name == 'posix' else 'cls')
    active_subdomains = []
    
    for sub in subdomain_list:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code < 400:
                print(f"[+] Found: {url}")
                active_subdomains.append(url)
        except requests.ConnectionError:
            pass
    
    return active_subdomains

#function to check for active directory
def directory_check(domain,directory_list):
    active_directory =[]
    
    for direc in directory_list:
        url = f"https://{domain}/{dir}"
        try:
            response = requests.get(url,timeout=2)
            if response == 200:
                print(f"[=] Found directory : {url}")
                active_directory.append(url)
        except requests.ConnectionError:
            pass
    return active_directory



# Read subdomains from file

def run_subdomain():
    domain=input(Fore.BLUE+"[+] Enter Domain Name :")
    print(Fore.BLUE + "[1] Subdomain scanning \n[2] Directory scanning")
    option = input(Fore.BLUE + "[?] Enter you choice :")
    
    if (option == "1"):
        with open("phantom_tool/subdomain.txt", "r") as file:
            subdomains = [line.strip() for line in file]
        found_subdomains = check_subdomain(domain, subdomains)
        for sub in found_subdomains:
            print(Fore.GREEN + f"{sub} \n")
        print(Fore.GREEN +"Scan completed.")

    elif (option == "2"):
        with open("phantom_tool/directory.txt","r") as file:
            directories = [line.strip() for line in file]
        found_directories =  directory_check(domain , directories)
        for direc in found_directories:
            print(Fore.GREEN + f"{direc} \n")
        print(Fore.GREEN+"Scan completed.")

'''