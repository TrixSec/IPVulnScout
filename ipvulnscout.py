from src.ip import fetch_vulnerabilities, get_ip_input as get_vuln_ip_input
from src.cve import get_cve_info, get_cve_input
from src.port import fetch_open_ports, get_ip_input as get_port_ip_input
from termcolor import colored
import os
import requests
import random
from config.config import IPVULNSCOUT_VERSION, print_banner
from src.reverse import reverse

menu_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

def check_for_updates():
    try:
        response = requests.get("https://raw.githubusercontent.com/TrixSec/IPVulnScout/main/VERSION")
        response.raise_for_status()
        latest_version = response.text.strip()

        if IPVULNSCOUT_VERSION != latest_version:
            print(colored(f"[•] New version available: {latest_version}. Updating...", 'yellow'))
            os.system('git reset --hard HEAD')
            os.system('git pull')
            with open('VERSION', 'w') as version_file:
                version_file.write(latest_version)
            print(colored("[•] Update completed. Please rerun IPVulnScout.", 'green'))
            exit()

        print(colored(f"[•] You are using the latest version: {latest_version}.", 'green'))
    except requests.RequestException as e:
        print(colored(f"[×] Error fetching the latest version: {e}. Please check your internet connection.", 'red'))

def main():
    print_banner()
    check_for_updates()

    while True:
        random_color = random.choice(menu_colors)
        
        print("\n" + "-" * 33)
        print(colored("|         Please select an option         |", random_color, attrs=['bold']))
        print(colored("|" + "*" * 31 + "|", random_color, attrs=['bold']))
        print(colored("| 1. IP Vulnerability Checking            |", random_color, attrs=['bold']))
        print(colored("| 2. CVE Information                      |", random_color, attrs=['bold']))
        print(colored("| 3. Open Ports Checking                  |", random_color, attrs=['bold']))
        print(colored("| 4. Reverse IP Lookup                    |", random_color, attrs=['bold']))
        print(colored("| 0. Exit                                 |", random_color, attrs=['bold']))
        print("-" * 33)

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print(colored("Invalid input. Please enter a number.", 'red'))
            continue

        if choice == 1:
            print(colored("\n[•] IP Vulnerability Checking", 'cyan'))
            ip = get_vuln_ip_input()
            fetch_vulnerabilities(ip)
        
        elif choice == 2:
            print(colored("\n[•] CVE Information", 'cyan'))
            cve_id = get_cve_input()
            get_cve_info(cve_id)

        elif choice == 3:
            print(colored("\n[•] Open Ports Checking", 'cyan'))
            ip = get_port_ip_input()
            fetch_open_ports(ip)

        elif choice == 4:
            print(colored("\n[•] Reverse IP Lookup", 'cyan'))
            reverse()
        
        elif choice == 0:
            print(colored("\nExiting IPVulnScout. Goodbye!", 'green'))
            break
        
        else:
            print(colored("Invalid choice. Please select a valid option.", 'red'))

if __name__ == "__main__":
    main()


