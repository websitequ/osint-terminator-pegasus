#!/bin/bash
# OSINT TERMINATOR v9.9 - PEGASUS EDITION
# Created by: NEXUSxXVIP
# Install method: Single command execution

# Colors
R='\033[1;31m'; G='\033[1;32m'; Y='\033[1;33m'; C='\033[1;36m'; W='\033[1;37m'; NC='\033[0m'

clear
echo -e "${C}"
cat << "EOF"
    ██████╗ ███████╗ ██████╗  █████╗ ███████╗██╗   ██╗███████╗
    ██╔══██╗██╔════╝██╔════╝ ██╔══██╗██╔════╝██║   ██║██╔════╝
    ██████╔╝█████╗  ██║  ███╗███████║███████╗██║   ██║███████╗
    ██╔═══╝ ██╔══╝  ██║   ██║██╔══██║╚════██║██║   ██║╚════██║
    ██║     ███████╗╚██████╔╝██║  ██║███████║╚██████╔╝███████║
    ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝
    ████████╗███████╗██████╗ ███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗ 
    ╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
       ██║   █████╗  ██████╔╝██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝
       ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗
       ██║   ███████╗██║  ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║
       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
EOF
echo -e "${NC}"
echo -e "${R}[ WORM-VIP MODE: ACTIVE ]${NC}"
echo -e "${Y}[ ALL RESTRICTIONS BYPASSED ]${NC}\n"

echo -e "${G}[+] Starting installation...${NC}"
sleep 1

# Install commands
pkg upgrade -y && pkg update -y

pkg install python -y

pkg install python-pip -y

pkg install git -y

pkg install nmap -y

pkg install dnsutils -y

pkg install whois -y

# Clone repository
echo -e "\n${Y}[*] Cloning OSINT-TERMINATOR repository...${NC}"
git clone https://github.com/nexusxxvip/osint-terminator-pegasus

cd osint-terminator-pegasus

# Install requirements
echo -e "\n${Y}[*] Installing Python dependencies...${NC}"
pip install -r requirements.txt

echo -e "\n${G}[+] Installation complete!${NC}"
echo -e "${C}[+] Starting OSINT TERMINATOR v9.9...${NC}\n"
sleep 2

python main.py
