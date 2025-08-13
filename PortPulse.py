import socket
import threading
import time
import sys
import os
from concurrent.futures import ThreadPoolExecutor
import ipaddress

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """

                                                                         










            
                                                                            
                                                                            
 ▀███▀▀▀██▄                   ██  ▀███▀▀▀██▄            ▀███                 
     ██   ▀██▄                  ██    ██   ▀██▄             ██                 
     ██   ▄██  ▄██▀██▄▀███▄███████    ██   ▄██▀███  ▀███    ██  ▄██▀███ ▄▄█▀██ 
     ███████  ██▀   ▀██ ██▀ ▀▀  ██    ███████   ██    ██    ██  ██   ▀▀▄█▀   ██
     ██       ██     ██ ██      ██    ██        ██    ██    ██  ▀█████▄██▀▀▀▀▀▀
    ██       ██▄   ▄██ ██      ██    ██        ██    ██    ██  █▄   ████▄    ▄
    ████▄      ▀█████▀▄████▄    ▀███ █████▄      ▀████▀███▄▄████▄██████▀ ▀█████▀
                                                                                                        
                                    [PortPulse v1.0]
                                    [Created by: AymanCsharp]
    """
    print(banner)

def scan_port(ip, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return port if result == 0 else None
    except:
        return None

def scan_single_port(ip, port):
    print(f"\n[*] Scanning port {port} on {ip}...")
    if scan_port(ip, port):
        print(f"[+] Port {port} is OPEN on {ip}")
        return True
    else:
        print(f"[-] Port {port} is CLOSED on {ip}")
        return False

def scan_port_range(ip, start_port, end_port, threads=100):
    print(f"\n[*] Scanning ports {start_port}-{end_port} on {ip} with {threads} threads...")
    open_ports = []
    
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port + 1)}
        
        for future in futures:
            port = futures[future]
            try:
                result = future.result()
                if result:
                    open_ports.append(result)
                    print(f"[+] Port {result} is OPEN on {ip}")
            except:
                pass
    
    if open_ports:
        print(f"\n[+] Found {len(open_ports)} open ports: {sorted(open_ports)}")
    else:
        print(f"\n[-] No open ports found in range {start_port}-{end_port}")
    
    return open_ports

def scan_common_ports(ip):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 993, 995, 1723, 3306, 3389, 5900, 8080]
    print(f"\n[*] Scanning {len(common_ports)} common ports on {ip}...")
    open_ports = []
    
    for port in common_ports:
        if scan_port(ip, port):
            open_ports.append(port)
            print(f"[+] Port {port} is OPEN on {ip}")
    
    if open_ports:
        print(f"\n[+] Found {len(open_ports)} open common ports: {open_ports}")
    else:
        print(f"\n[-] No open common ports found")
    
    return open_ports

def scan_all_ports(ip, threads=1000):
    print(f"\n[*] Scanning ALL ports (1-65535) on {ip} with {threads} threads...")
    print("[!] This may take a while...")
    
    open_ports = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in range(1, 65536)}
        
        for future in futures:
            port = futures[future]
            try:
                result = future.result()
                if result:
                    open_ports.append(result)
                    print(f"[+] Port {result} is OPEN on {ip}")
            except:
                pass
    
    if open_ports:
        print(f"\n[+] Found {len(open_ports)} open ports: {sorted(open_ports)}")
    else:
        print(f"\n[-] No open ports found")
    
    return open_ports

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False

def validate_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except:
        return False

def main():
    while True:
        clear_screen()
        print_banner()
        
        print("\n" + "="*70)
        print("                           SCANNING OPTIONS")
        print("="*70)
        print("1  - Scan Single Port")
        print("2  - Scan Port Range")
        print("3  - Scan Common Ports")
        print("4  - Scan All Ports (1-65535)")
        print("5  - Custom Port List Scan")
        print("6  - Fast Network Discovery")
        print("7  - Service Detection")
        print("8  - Export Results")
        print("9  - Settings")
        print("10 - Exit")
        print("="*70)
        
        try:
            choice = input("\nWhat Number You Want: ").strip()
            
            if choice == "1":
                ip = input("\nEnter IP Address: ").strip()
                if not validate_ip(ip):
                    print("[-] Invalid IP address!")
                    input("\nPress Enter to continue...")
                    continue
                
                port = input("Enter Port Number (1-65535): ").strip()
                if not validate_port(port):
                    print("[-] Invalid port number!")
                    input("\nPress Enter to continue...")
                    continue
                
                scan_single_port(ip, int(port))
                
            elif choice == "2":
                ip = input("\nEnter IP Address: ").strip()
                if not validate_ip(ip):
                    print("[-] Invalid IP address!")
                    input("\nPress Enter to continue...")
                    continue
                
                start_port = input("Enter Start Port (1-65535): ").strip()
                end_port = input("Enter End Port (1-65535): ").strip()
                
                if not validate_port(start_port) or not validate_port(end_port):
                    print("[-] Invalid port range!")
                    input("\nPress Enter to continue...")
                    continue
                
                start_port, end_port = int(start_port), int(end_port)
                if start_port > end_port:
                    start_port, end_port = end_port, start_port
                
                threads = input("Enter number of threads (default 100): ").strip()
                threads = int(threads) if threads.isdigit() else 100
                
                scan_port_range(ip, start_port, end_port, threads)
                
            elif choice == "3":
                ip = input("\nEnter IP Address: ").strip()
                if not validate_ip(ip):
                    print("[-] Invalid IP address!")
                    input("\nPress Enter to continue...")
                    continue
                
                scan_common_ports(ip)
                
            elif choice == "4":
                ip = input("\nEnter IP Address: ").strip()
                if not validate_ip(ip):
                    print("[-] Invalid IP address!")
                    input("\nPress Enter to continue...")
                    continue
                
                confirm = input("Are you sure? This will scan ALL 65535 ports! (y/N): ").strip().lower()
                if confirm == 'y':
                    threads = input("Enter number of threads (default 1000): ").strip()
                    threads = int(threads) if threads.isdigit() else 1000
                    scan_all_ports(ip, threads)
                else:
                    print("[-] Scan cancelled.")
                
            elif choice == "5":
                ip = input("\nEnter IP Address: ").strip()
                if not validate_ip(ip):
                    print("[-] Invalid IP address!")
                    input("\nPress Enter to continue...")
                    continue
                
                ports_input = input("Enter ports separated by comma (e.g., 80,443,8080): ").strip()
                try:
                    ports = [int(p.strip()) for p in ports_input.split(',') if p.strip().isdigit()]
                    if not ports:
                        print("[-] No valid ports entered!")
                        input("\nPress Enter to continue...")
                        continue
                    
                    print(f"\n[*] Scanning {len(ports)} custom ports on {ip}...")
                    open_ports = []
                    for port in ports:
                        if scan_port(ip, port):
                            open_ports.append(port)
                            print(f"[+] Port {port} is OPEN on {ip}")
                    
                    if open_ports:
                        print(f"\n[+] Found {len(open_ports)} open ports: {open_ports}")
                    else:
                        print(f"\n[-] No open ports found")
                        
                except:
                    print("[-] Invalid port format!")
                    input("\nPress Enter to continue...")
                    continue
                
            elif choice == "6":
                print("\n[*] Fast Network Discovery")
                print("[!] This feature scans common ports on multiple IPs in a range")
                network = input("Enter network (e.g., 192.168.1.0/24): ").strip()
                try:
                    network_obj = ipaddress.ip_network(network, strict=False)
                    print(f"[*] Scanning {network_obj.num_addresses} IPs...")
                    
                    for ip in list(network_obj.hosts())[:10]:
                        print(f"\n[*] Scanning {ip}")
                        open_ports = scan_common_ports(str(ip))
                        if open_ports:
                            print(f"[+] {ip} has {len(open_ports)} open ports")
                        
                        if input("\nContinue scanning? (y/N): ").strip().lower() != 'y':
                            break
                            
                except:
                    print("[-] Invalid network format!")
                    input("\nPress Enter to continue...")
                    continue
                
            elif choice == "7":
                print("\n[*] Service Detection")
                print("[!] This feature identifies services running on open ports")
                ip = input("Enter IP Address: ").strip()
                if not validate_ip(ip):
                    print("[-] Invalid IP address!")
                    input("\nPress Enter to continue...")
                    continue
                
                print(f"\n[*] Detecting services on {ip}...")
                common_services = {
                    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
                    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 3306: "MySQL",
                    3389: "RDP", 8080: "HTTP-Proxy"
                }
                
                for port, service in common_services.items():
                    if scan_port(ip, port):
                        print(f"[+] Port {port} ({service}) is OPEN on {ip}")
                
            elif choice == "8":
                print("\n[*] Export Results")
                print("[!] This feature saves scan results to a file")
                filename = input("Enter filename (default: scan_results.txt): ").strip()
                if not filename:
                    filename = "scan_results.txt"
                
                print(f"[+] Results will be saved to {filename}")
                print("[!] Run a scan first to have results to export")
                
            elif choice == "9":
                print("\n[*] Settings")
                print("1 - Change default timeout")
                print("2 - Change default threads")
                print("3 - Back to main menu")
                
                setting_choice = input("\nWhat Number You Want: ").strip()
                if setting_choice == "1":
                    timeout = input("Enter new timeout in seconds (default 1): ").strip()
                    print(f"[+] Timeout set to {timeout} seconds")
                elif setting_choice == "2":
                    threads = input("Enter new default threads (default 100): ").strip()
                    print(f"[+] Default threads set to {threads}")
                
            elif choice == "10":
                print("\n[*] Exiting TPortScanner...")
                print("[+] Thank you for using TPortScanner!")
                sys.exit(0)
                
            else:
                print("[-] Invalid choice! Please select 1-10.")
                
        except KeyboardInterrupt:
            print("\n\n[!] Scan interrupted by user")
        except Exception as e:
            print(f"\n[-] Error: {e}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] TPortScanner terminated by user")
        sys.exit(0)

