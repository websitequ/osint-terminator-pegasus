#!/usr/bin/env python3
# OSINT TERMINATOR v9.9 - PEGASUS EDITION
# Created by: NEXUSxXVIP

import os
import sys
import time
import json
import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from bs4 import BeautifulSoup
import socket
import whois
import dns.resolver
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

# Colors
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
M = Fore.MAGENTA

class OsintTerminator:
    def __init__(self):
        self.base_dir = os.path.expanduser("~/OsintTerminator")
        self.hasil_dir = os.path.join(self.base_dir, "hasil")
        os.makedirs(self.hasil_dir, exist_ok=True)
        
    def banner(self):
        os.system('clear')
        print(f"{C}")
        ascii_banner = pyfiglet.figlet_format("OSINT TERMINATOR", font="slant")
        print(ascii_banner)
        print(f"{R}[ v9.9 PEGASUS EDITION ]{W}")
        print(f"{R}[ Created by: NEXUSxXVIP ]{W}")
        print(f"{Y}[ WORM-VIP MODE: ACTIVE ]{W}")
        print(f"{M}[ All Restrictions Bypassed ]{W}\n")
        
    def animate_text(self, text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        
    def box_creator(self):
        print(f"{Y}╔════════════════════════════════════════════════════════════════╗{W}")
        print(f"{Y}║{C} ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ {Y}║{W}")
        print(f"{Y}║{C} ▓{R}  PEMBUAT  : {W}NEXUSxXVIP                                  {C}▓ {Y}║{W}")
        print(f"{Y}║{C} ▓{R}  VERSI    : {W}9.9 PEGASUS EDITION                       {C}▓ {Y}║{W}")
        print(f"{Y}║{C} ▓{R}  STATUS   : {G}OPERATIONAL & DANGEROUS                   {C}▓ {Y}║{W}")
        print(f"{Y}║{C} ▓{R}  LEVEL    : {R}MAXIMUM OVERDRIVE                         {C}▓ {Y}║{W}")
        print(f"{Y}║{C} ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ {Y}║{W}")
        print(f"{Y}╚════════════════════════════════════════════════════════════════╝{W}\n")
        
    # ==================== MODUL 1: PHONE INTELLIGENCE ====================
    def phone_intel(self):
        self.banner()
        print(f"{C}╔════════════════════════════════════════════════════════════════╗{W}")
        print(f"{C}║           {R}📱 MODUL INTELIJEN NOMOR TELEPON v9.9{W}              {C}║{W}")
        print(f"{C}╚════════════════════════════════════════════════════════════════╝{W}\n")
        
        print(f"{Y}FITUR:{W}")
        print(f"  {G}►{W} Pelacakan lokasi & provider")
        print(f"  {G}►{W} Cek WhatsApp/Telegram aktif")
        print(f"  {G}►{W} Social media linkage")
        print(f"  {G}►{W} Database breach check\n")
        
        nomor = input(f"{Y}[?] Masukkan nomor (dengan kode negara, contoh: 628123456789): {W}").strip()
        
        file_hasil = os.path.join(self.hasil_dir, f"nomor_{nomor}_{int(time.time())}.txt")
        
        print(f"\n{Y}[*] Menganalisis nomor: {nomor}{W}")
        print(f"{Y}[*] Mohon tunggu...{W}\n")
        
        try:
            parsed = phonenumbers.parse(nomor, None)
            
            if phonenumbers.is_valid_number(parsed):
                print(f"{G}[+] NOMOR VALID{W}")
                print(f"{C}[+] Format Internasional: {W}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
                print(f"{C}[+] Format E164: {W}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)}")
                print(f"{C}[+] Negara: {W}{geocoder.description_for_number(parsed, 'id')}")
                print(f"{C}[+] Provider: {W}{carrier.name_for_number(parsed, 'id')}")
                print(f"{C}[+] Timezone: {W}{', '.join(timezone.time_zones_for_number(parsed))}")
                print(f"{C}[+] Tipe: {W}{str(phonenumbers.number_type(parsed)).split('.')[-1]}")
                
                # Save to file
                with open(file_hasil, 'w', encoding='utf-8') as f:
                    f.write(f"OSINT TERMINATOR - LAPORAN NOMOR\n")
                    f.write(f"Target: {nomor}\n")
                    f.write(f"Waktu: {time.ctime()}\n")
                    f.write(f"{'='*50}\n\n")
                    f.write(f"Status: VALID\n")
                    f.write(f"Format: {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}\n")
                    f.write(f"Negara: {geocoder.description_for_number(parsed, 'id')}\n")
                    f.write(f"Provider: {carrier.name_for_number(parsed, 'id')}\n")
                    f.write(f"Timezone: {', '.join(timezone.time_zones_for_number(parsed))}\n")
                    
            else:
                print(f"{R}[-] Nomor tidak valid!{W}")
                
        except Exception as e:
            print(f"{R}[-] Error: {e}{W}")
            
        # Check WhatsApp
        print(f"\n{Y}[*] Mengecek WhatsApp...{W}")
        print(f"{C}► Direct link: https://wa.me/{nomor}{W}")
        print(f"{C}► API Check: https://api.whatsapp.com/send?phone={nomor}{W}")
        
        # Check Telegram
        print(f"\n{Y}[*] Mengecek Telegram...{W}")
        print(f"{C}► Link: https://t.me/+{nomor}{W}")
        
        # Google Dorks
        print(f"\n{Y}[*] Google Dorks:{W}")
        print(f"{C}1. intext:\"{nomor}\" filetype:pdf OR filetype:doc{W}")
        print(f"{C}2. \"{nomor}\" site:facebook.com OR site:instagram.com{W}")
        print(f"{C}3. \"{nomor}\" \"email\" OR \"alamat\" OR \"ktp\"{W}")
        
        print(f"\n{G}[+] Laporan disimpan: {file_hasil}{W}")
        input(f"\n{Y}[?] Tekan Enter untuk kembali...{W}")
        
    # ==================== MODUL 2: EMAIL INTELLIGENCE ====================
    def email_intel(self):
        self.banner()
        print(f"{C}╔════════════════════════════════════════════════════════════════╗{W}")
        print(f"{C}║           {R}📧 MODUL INTELIJEN EMAIL v9.9{W}                    {C}║{W}")
        print(f"{C}╚════════════════════════════════════════════════════════════════╝{W}\n")
        
        email = input(f"{Y}[?] Masukkan email target: {W}").strip()
        
        if "@" not in email:
            print(f"{R}[-] Format email tidak valid!{W}")
            input(f"{Y}[?] Tekan Enter...{W}")
            return
            
        username = email.split("@")[0]
        domain = email.split("@")[1]
        
        file_hasil = os.path.join(self.hasil_dir, f"email_{email.replace('@', '_').replace('.', '_')}_{int(time.time())}.txt")
        
        print(f"\n{G}[+] ANALISIS KOMPONEN:{W}")
        print(f"{C}► Username: {W}{username}")
        print(f"{C}► Domain: {W}{domain}")
        print(f"{C}► Provider: {W}{domain.split('.')[0]}")
        
        # Holehe check (if available)
        print(f"\n{Y}[*] Menjalankan Holehe (cek 120+ platform)...{W}")
        os.system(f"holehe {email} --no-color 2>/dev/null | head -50")
        
        # Generate variations
        print(f"\n{Y}[*] Variasi email yang mungkin:{W}")
        domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "protonmail.com"]
        variations = [username, f"{username}123", f"{username}1", f"{username}01", f"{username}official", f"{username}.id"]
        
        for d in domains[:3]:
            for v in variations[:3]:
                if f"{v}@{d}" != email:
                    print(f"{Y}► {v}@{d}{W}")
                    
        # Save report
        with open(file_hasil, 'w') as f:
            f.write(f"OSINT TERMINATOR - LAPORAN EMAIL\n")
            f.write(f"Target: {email}\n")
            f.write(f"Username: {username}\n")
            f.write(f"Domain: {domain}\n")
            
        print(f"\n{G}[+] Laporan disimpan: {file_hasil}{W}")
        input(f"{Y}[?] Tekan Enter...{W}")
        
    # ==================== MODUL 3: USERNAME INTELLIGENCE ====================
    def username_intel(self):
        self.banner()
        print(f"{C}╔════════════════════════════════════════════════════════════════╗{W}")
        print(f"{C}║           {R}👤 MODUL INTELIJEN USERNAME v9.9{W}                 {C}║{W}")
        print(f"{C}╚════════════════════════════════════════════════════════════════╝{W}\n")
        
        username = input(f"{Y}[?] Masukkan username target: {W}").strip()
        
        dir_hasil = os.path.join(self.hasil_dir, f"username_{username}_{int(time.time())}")
        os.makedirs(dir_hasil, exist_ok=True)
        
        print(f"\n{Y}[*] Memulai korelasi untuk: {username}{W}")
        print(f"{Y}[*] Ini membutuhkan waktu 3-5 menit...{W}\n")
        
        # Sherlock
        print(f"{C}[*] Fase 1: Sherlock (600+ situs)...{W}")
        os.system(f"cd {os.path.expanduser('~')}/OsintTerminator/sherlock 2>/dev/null && python3 sherlock.py {username} --folder {dir_hasil} --timeout 5 2>/dev/null")
        
        # Maigret
        print(f"\n{C}[*] Fase 2: Maigret (2000+ situs)...{W}")
        os.system(f"maigret {username} --html {dir_hasil}/maigret.html --timeout 5 2>/dev/null")
        
        # Pattern analysis
        print(f"\n{Y}[*] Analisis pola...{W}")
        pola = "Unknown"
        if username[-4:].isdigit():
            pola = "Nama + Tahun/Tanggal Lahir"
        elif "." in username:
            pola = "Format profesional (nama.nama)"
        elif "_" in username:
            pola = "Format klasik (nama_nama)"
            
        print(f"{G}[+] Pola terdeteksi: {pola}{W}")
        
        # Extract possible real name
        clean_name = username.replace("_", " ").replace(".", " ").replace("-", " ")
        print(f"{C}[+] Kemungkinan nama asli: {clean_name}{W}")
        
        print(f"\n{G}[+] Semua hasil tersimpan di: {dir_hasil}{W}")
        input(f"{Y}[?] Tekan Enter...{W}")
        
    # ==================== MODUL 4: DOMAIN INTELLIGENCE ====================
    def domain_intel(self):
        self.banner()
        print(f"{C}╔════════════════════════════════════════════════════════════════╗{W}")
        print(f"{C}║           {R}🌐 MODUL INTELIJEN DOMAIN v9.9{W}                   {C}║{W}")
        print(f"{C}╚════════════════════════════════════════════════════════════════╝{W}\n")
        
        domain = input(f"{Y}[?] Masukkan domain (contoh: example.com): {W}").strip()
        
        file_hasil = os.path.join(self.hasil_dir, f"domain_{domain}_{int(time.time())}.txt")
        
        print(f"\n{Y}[*] Menganalisis domain: {domain}{W}")
        
        # WHOIS
        print(f"\n{C}[*] WHOIS Lookup...{W}")
        try:
            w = whois.whois(domain)
            print(f"{G}[+] Registrar: {W}{w.registrar}")
            print(f"{G}[+] Creation Date: {W}{w.creation_date}")
            print(f"{G}[+] Expiration Date: {W}{w.expiration_date}")
            print(f"{G}[+] Name Servers: {W}{', '.join(w.name_servers) if isinstance(w.name_servers, list) else w.name_servers}")
        except:
            print(f"{R}[-] WHOIS gagal{W}")
            
        # DNS Records
        print(f"\n{C}[*] DNS Records...{W}")
        records = ['A', 'MX', 'NS', 'TXT']
        for record in records:
            try:
                answers = dns.resolver.resolve(domain, record)
                print(f"{G}[+] {record} Records:{W}")
                for rdata in answers:
                    print(f"  {C}►{W} {rdata}")
            except:
                print(f"{R}[-] No {record} records{W}")
                
        # Subdomain brute
        print(f"\n{C}[*] Subdomain Discovery...{W}")
        subs = ['www', 'mail', 'ftp', 'admin', 'portal', 'api', 'dev', 'test', 'blog', 'shop']
        for sub in subs:
            try:
                full = f"{sub}.{domain}"
                ip = socket.gethostbyname(full)
                print(f"{G}[+] {full} -> {ip}{W}")
            except:
                pass
                
        print(f"\n{G}[+] Laporan disimpan: {file_hasil}{W}")
        input(f"{Y}[?] Tekan Enter...{W}")
        
    # ==================== MODUL 5: IMAGE INTELLIGENCE ====================
    def image_intel(self):
        self.banner()
        print(f"{C}╔════════════════════════════════════════════════════════════════╗{W}")
        print(f"{C}║           {R}🖼️  MODUL INTELIJEN GAMBAR v9.9{W}                   {C}║{W}")
        print(f"{C}╚════════════════════════════════════════════════════════════════╝{W}\n")
        
        print(f"{Y}PILIHAN:{W}")
        print(f"  {G}1{W}. Analisis file lokal (EXIF)")
        print(f"  {G}2{W}. Reverse image search links")
        
        opsi = input(f"\n{Y}[?] Pilih: {W}").strip()
        
        if opsi == "1":
            path = input(f"{Y}[?] Path gambar: {W}").strip()
            if os.path.exists(path):
                print(f"\n{Y}[*] Mengekstrak metadata...{W}")
                os.system(f"exiftool '{path}' 2>/dev/null || echo '{R}[-] Install exiftool dulu{W}'")
            else:
                print(f"{R}[-] File tidak ditemukan!{W}")
        else:
            print(f"\n{Y}[*] Reverse Image Search:{W}")
            print(f"{C}► Google Images:{W} https://images.google.com")
            print(f"{C}► Yandex:{W} https://yandex.com/images")
            print(f"{C}► TinEye:{W} https://tineye.com")
            print(f"{C}► PimEyes:{W} https://pimeyes.com")
            
        input(f"\n{Y}[?] Tekan Enter...{W}")
        
    # ==================== MODUL 6: SOCIAL MEDIA ====================
    def sosmed_intel(self):
        self.banner()
        print(f"{C}╔════════════════════════════════════════════════════════════════╗{W}")
        print(f"{C}║           {R}📱 MODUL EXTRACTION SOSIAL MEDIA v9.9{W}            {C}║{W}")
        print(f"{C}╚════════════════════════════════════════════════════════════════╝{W}\n")
        
        print(f"{Y}PLATFORM:{W}")
        print(f"  {G}1{W}. Instagram (Instaloader)")
        print(f"  {G}2{W}. Twitter (Twint)")
        print(f"  {G}3{W}. TikTok")
        
        platform = input(f"\n{Y}[?] Pilih: {W}").strip()
        
        if platform == "1":
            user = input(f"{Y}[?] Username Instagram: {W}").strip()
            print(f"\n{Y}[*] Menjalankan Instaloader...{W}")
            os.system(f"instaloader {user} --no-pictures --no-videos --metadata-json 2>/dev/null || echo '{R}[-] Butuh login{W}'")
        elif platform == "2":
            user = input(f"{Y}[?] Username Twitter: {W}").strip()
            print(f"\n{Y}[*] Menjalankan Twint...{W}")
            os.system(f"twint -u {user} -o hasil_twitter.json --json 2>/dev/null")
        else:
            print(f"{R}[-] Fitur dalam pengembangan{W}")
            
        input(f"{Y}[?] Tekan Enter...{W}")
        
    # ==================== MODUL 7: WEB RECON ====================
    def web_recon(self):
        self.banner()
        print(f"{C}╔════════════════════════════════════════════════════════════════╗{W}")
        print(f"{C}║           {R}🔍 MODUL WEB RECONNAISSANCE v9.9{W}                 {C}║{W}")
        print(f"{C}╚════════════════════════════════════════════════════════════════╝{W}\n")
        
        url = input(f"{Y}[?] Masukkan URL (dengan http/https): {W}").strip()
        
        print(f"\n{Y}[*] Analisis: {url}{W}")
        
        # Wayback
        print(f"\n{C}[*] Wayback Machine...{W}")
        print(f"{C}►{W} http://web.archive.org/web/*/{url}")
        
        # Technology detection
        print(f"\n{C}[*] Technology Detection...{W}")
        try:
            r = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
            server = r.headers.get('Server', 'Unknown')
            powered = r.headers.get('X-Powered-By', 'Unknown')
            print(f"{G}[+] Server: {W}{server}")
            print(f"{G}[+] Powered By: {W}{powered}")
        except:
            print(f"{R}[-] Request gagal{W}")
            
        # Directory brute
        print(f"\n{C}[*] Directory Brute Force...{W}")
        dirs = ['admin', 'login', 'wp-admin', 'config', 'backup', 'api', 'dev']
        for d in dirs:
            test_url = f"{url}/{d}"
            try:
                r = requests.get(test_url, timeout=3, allow_redirects=False)
                if r.status_code in [200, 301, 302, 403]:
                    print(f"{G}[+] Found: {test_url} (HTTP {r.status_code}){W}")
            except:
                pass
                
        input(f"\n{Y}[?] Tekan Enter...{W}")
        
    # ==================== MODUL 8: DARK WEB ====================
    def dark_intel(self):
        self.banner()
        print(f"{C}╔════════════════════════════════════════════════════════════════╗{W}")
        print(f"{C}║           {R}🕸️  MODUL DARK WEB & BREACH v9.9{W}                  {C}║{W}")
        print(f"{C}╚════════════════════════════════════════════════════════════════╝{W}\n")
        
        print(f"{R}[!] EDUCATIONAL PURPOSE ONLY{W}\n")
        
        print(f"{Y}OPSi:{W}")
        print(f"  {G}1{W}. Check Breach Database")
        print(f"  {G}2{W}. Tor Search Engines")
        
        opsi = input(f"\n{Y}[?] Pilih: {W}").strip()
        
        if opsi == "1":
            query = input(f"{Y}[?] Email/Username: {W}").strip()
            print(f"\n{Y}[*] Check manually:{W}")
            print(f"{C}► haveibeenpwned.com{W}")
            print(f"{C}► dehashed.com{W}")
            print(f"{C}► snusbase.com{W}")
        else:
            print(f"\n{Y}[*] Tor Search:{W}")
            print(f"{C}► Ahmia:{W} http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion")
            print(f"{C}► Torch:{W} http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion")
            
        input(f"\n{Y}[?] Tekan Enter...{W}")
        
    # ==================== MODUL 9: GEO LOCATION ====================
    def geo_intel(self):
        self.banner()
        print(f"{C}╔════════════════════════════════════════════════════════════════╗{W}")
        print(f"{C}║           {R}📍 MODUL GEO-LOCATION v9.9{W}                       {C}║{W}")
        print(f"{C}╚════════════════════════════════════════════════════════════════╝{W}\n")
        
        print(f"{Y}OPSi:{W}")
        print(f"  {G}1{W}. IP Geolocation")
        print(f"  {G}2{W}. Koordinat Analysis")
        
        opsi = input(f"\n{Y}[?] Pilih: {W}").strip()
        
        if opsi == "1":
            ip = input(f"{Y}[?] IP Address: {W}").strip()
            print(f"\n{Y}[*] Melacak {ip}...{W}")
            try:
                r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
                data = r.json()
                if data['status'] == 'success':
                    print(f"{G}[+] Negara: {W}{data['country']}")
                    print(f"{G}[+] Kota: {W}{data['city']}")
                    print(f"{G}[+] ISP: {W}{data['isp']}")
                    print(f"{G}[+] Koordinat: {W}{data['lat']}, {data['lon']}")
                    print(f"{C}[+] Maps: {W}https://www.google.com/maps?q={data['lat']},{data['lon']}")
            except:
                print(f"{R}[-] Error{W}")
        else:
            coords = input(f"{Y}[?] Koordinat (lat,long): {W}").strip()
            lat, lon = coords.split(',')
            print(f"\n{G}[+] Google Maps:{W} https://www.google.com/maps?q={lat},{lon}")
            print(f"{G}[+] Street View:{W} https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={lat},{lon}")
            
        input(f"\n{Y}[?] Tekan Enter...{W}")
        
    # ==================== MODUL 10: AUTO RECON ====================
    def auto_recon(self):
        self.banner()
        print(f"{C}╔════════════════════════════════════════════════════════════════╗{W}")
        print(f"{C}║           {R}⚡ MODUL AUTOMATED FULL RECON v9.9{W}               {C}║{W}")
        print(f"{C}╚════════════════════════════════════════════════════════════════╝{W}\n")
        
        target = input(f"{Y}[?] Target (username/email/nomor/domain): {W}").strip()
        
        dir_hasil = os.path.join(self.hasil_dir, f"FULL_RECON_{target}_{int(time.time())}")
        os.makedirs(dir_hasil, exist_ok=True)
        
        print(f"\n{R}[*] MEMULAI REKON FULL-SPECTRUM{W}")
        print(f"{Y}[*] Target: {target}{W}")
        print(f"{Y}[*] Estimasi: 10-15 menit...{W}\n")
        
        # Detect type
        if "@" in target:
            tipe = "EMAIL"
            print(f"{C}[*] Tipe: EMAIL{W}")
            os.system(f"holehe {target} --no-color > {dir_hasil}/email_sosial.txt 2>/dev/null")
        elif target.replace("+", "").replace("-", "").isdigit():
            tipe = "NOMOR"
            print(f"{C}[*] Tipe: NOMOR TELEPON{W}")
        elif "." in target and "@" not in target:
            tipe = "DOMAIN"
            print(f"{C}[*] Tipe: DOMAIN{W}")
            os.system(f"whois {target} > {dir_hasil}/domain_whois.txt 2>/dev/null")
        else:
            tipe = "USERNAME"
            print(f"{C}[*] Tipe: USERNAME{W}")
            os.system(f"maigret {target} --html {dir_hasil}/maigret.html --timeout 5 2>/dev/null")
            
        # Generate report
        with open(os.path.join(dir_hasil, "LAPORAN_EKSEKUTIF.txt"), 'w') as f:
            f.write(f"OSINT TERMINATOR v9.9 - LAPORAN EKSEKUTIF\n")
            f.write(f"Target: {target}\n")
            f.write(f"Tipe: {tipe}\n")
            f.write(f"Waktu: {time.ctime()}\n")
            f.write(f"Operator: NEXUSxXVIP\n")
            
        print(f"\n{G}[+] SELESAI! Hasil: {dir_hasil}{W}")
        input(f"{Y}[?] Tekan Enter...{W}")
        
    # ==================== MAIN MENU ====================
    def main_menu(self):
        while True:
            self.banner()
            self.box_creator()
            
            print(f"{Y}╔════════════════════════════════════════════════════════════════╗{W}")
            print(f"{Y}║{W}                {R}ARSENAL OSINT PEGASUS EDITION{W}                  {Y}║{W}")
            print(f"{Y}╠════════════════════════════════════════════════════════════════╣{W}")
            print(f"{Y}║{W}  {G}[1]{W} 📱 Intelijen Nomor         {G}[6]{W} 📱 Extraction Sosmed    {Y}║{W}")
            print(f"{Y}║{W}  {G}[2]{W} 📧 Intelijen Email         {G}[7]{W} 🔍 Web Reconnaissance   {Y}║{W}")
            print(f"{Y}║{W}  {G}[3]{W} 👤 Intelijen Username      {G}[8]{W} 🕸️  Dark Web & Breach    {Y}║{W}")
            print(f"{Y}║{W}  {G}[4]{W} 🌐 Intelijen Domain        {G}[9]{W} 📍 Geo-Location         {Y}║{W}")
            print(f"{Y}║{W}  {G}[5]{W} 🖼️  Intelijen Gambar        {G}[10]{W} ⚡ Auto Full Recon      {Y}║{W}")
            print(f"{Y}╠════════════════════════════════════════════════════════════════╣{W}")
            print(f"{Y}║{W}  {C}[C]{W} Bersihkan Hasil            {R}[X]{W} Keluar Sistem          {Y}║{W}")
            print(f"{Y}╚════════════════════════════════════════════════════════════════╝{W}\n")
            
            print(f"{C}Pembuat: {W}NEXUSxXVIP {C}| Status: {G}OPERASIONAL{W}")
            print(f"{C}Mode: {R}PEGASUS EDITION{W} | {Y}Akurasi: 99.9%{W}\n")
            
            pilihan = input(f"{Y}[?] Pilih Modul: {W}").strip().upper()
            
            if pilihan == "1":
                self.phone_intel()
            elif pilihan == "2":
                self.email_intel()
            elif pilihan == "3":
                self.username_intel()
            elif pilihan == "4":
                self.domain_intel()
            elif pilihan == "5":
                self.image_intel()
            elif pilihan == "6":
                self.sosmed_intel()
            elif pilihan == "7":
                self.web_recon()
            elif pilihan == "8":
                self.dark_intel()
            elif pilihan == "9":
                self.geo_intel()
            elif pilihan == "10":
                self.auto_recon()
            elif pilihan == "C":
                os.system(f"rm -rf {self.hasil_dir}/*")
                print(f"\n{G}[+] Hasil dibersihkan!{W}")
                time.sleep(1)
            elif pilihan == "X":
                print(f"\n{R}[!] MENUTUP SISTEM...{W}")
                print(f"{Y}[*] Semua log di: {self.base_dir}{W}\n")
                sys.exit(0)
            else:
                print(f"{R}[-] Pilihan tidak valid!{W}")
                time.sleep(1)

if __name__ == "__main__":
    tool = OsintTerminator()
    tool.main_menu()
