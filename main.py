# port_scan.py
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

ports_status = []

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        return port, "Open"
    except:
        return port, "Closed"
    finally:
        s.close()

def run_port_scan(ip, port_list, max_threads=100):
    results = []
    with ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in port_list]
        for f in as_completed(futures):
            port, status = f.result()
            print(f"[+] Port {port}: {status}")
            results.append((port, status))
    return results


target_ip = "spsbbk.edu.in"
ports = range(1, 100)
run_port_scan(target_ip, ports)