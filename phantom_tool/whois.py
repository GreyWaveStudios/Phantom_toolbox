import socket
from colorama import Fore
import os

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

def extract_tld(domain):
    os.system('clear' if os.name == 'posix' else 'cls')
    parts = domain.lower().split('.')
    if len(parts) >= 3:
        sub_tld = "." + parts[-2] + "." + parts[-1]  # e.g., .edu.in
        if sub_tld in whois_servers:
            return sub_tld
    if len(parts) >= 2:
        tld = "." + parts[-1]  # e.g., .com
        if tld in whois_servers:
            return tld
    return None

def whois_lookup(domain):
    os.system('clear' if os.name == 'posix' else 'cls')
    tld = extract_tld(domain)
    if not tld:
        return f"[-] Unsupported or unknown TLD for domain '{domain}'."

    server = whois_servers[tld]
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server, 43))
            s.sendall((domain + "\r\n").encode())
            response = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                response += data
        return response.decode(errors="ignore")
    except Exception as e:
        return f"[!] Error connecting to WHOIS server: {e}"

def whois_main():
    domain = input(Fore.BLUE + "Enter the domain name: ").strip()
    print(Fore.GREEN + f"[+] Performing WHOIS lookup for: {domain}")
    result = whois_lookup(domain)
    print(Fore.GREEN + f"{result}")
