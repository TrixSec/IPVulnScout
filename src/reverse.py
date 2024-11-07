import requests
import random
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
import tldextract
import os
from config.config import REVERSE_URL
from config.config import MAX_COUNT
from config.config import display_banner

init(autoreset=True)
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
prompt_color = random.choice(colors)

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
]

def load_existing_domains(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding="utf-8") as file:
            return set(line.strip() for line in file)
    return set()

def save_domains(domains, filename, format_option):
    domains = list(domains)
    
    with open(filename, 'a') as file:
        for domain in domains[:MAX_COUNT]: 
            if format_option == 1:
                file.write(f"{domain}\n")
            elif format_option == 2:
                file.write(f"http://{domain}\n")
            elif format_option == 3:
                file.write(f"https://{domain}\n")
    
    print(f"{len(domains[:MAX_COUNT])} new domains saved in {filename}.")


def extract_domain(domain):
    ext = tldextract.extract(domain)
    return f"{ext.domain}.{ext.suffix}"

def fetch_reverseip(ip):
    url = REVERSE_URL.format(ip=ip)
    headers = {"User-Agent": random.choice(user_agents)}
    domains = []

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        raw_domains = [td.text for td in soup.select("table.table td")]
        
        domains = list(set(extract_domain(d) for d in raw_domains if "." in d))
        print(f"{prompt_color}[Rapiddns] Found {len(domains)} unique domains for IP: {ip}")
    except Exception as e:
        print(f"{prompt_color}[Error] Failed to fetch from RapidDNS: {e}")

    return domains

def reverse():
    display_banner()

    ip = input(f"{prompt_color}Enter a single IP to reverse lookup: {Style.BRIGHT}")
    filename = f"reverseip_{ip}.txt"
    
    domains = fetch_reverseip(ip)
    existing_domains = load_existing_domains(filename)
    new_domains = set(domains) - existing_domains
    
    if not new_domains:
        print(f"{prompt_color}No new domains to save for IP {ip}")
        return

    print(f"\n{prompt_color}Choose the saving format:")
    print(f"1 - Direct domain saving")
    print(f"2 - Save with http://")
    print(f"3 - Save with https://")
    print(f"4 - Don’t save, just print the result")
    print(f"5 - Exit without saving or printing")

    try:
        format_option = int(input(f"{prompt_color}Enter your choice (1-5): {Style.BRIGHT}"))
        if format_option == 4:
            print(f"\n{prompt_color}Domains found:")
            for domain in new_domains:
                print(domain)
        elif format_option == 5:
            print(f"{prompt_color}Exiting without saving or displaying domains.")
        elif format_option in [1, 2, 3]:
            save_domains(new_domains, filename, format_option)
        else:
            print(f"{prompt_color}Invalid choice. Exiting.")
    except ValueError:
        print(f"{prompt_color}Invalid input. Exiting.")
