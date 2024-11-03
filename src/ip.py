import requests
import re
import json
from colorama import Fore, Style, init
from config.config import BASE_URL, HEADERS

init(autoreset=True)

def fetch_vulnerabilities(ip):    
    url = f"{BASE_URL}/{ip}"

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[Error]{Style.RESET_ALL} Could not retrieve data: {e}")
        return None

    vulns_pattern = re.compile(r'const VULNS = ({.*?});', re.DOTALL)

    # Extract VULNS data
    match = vulns_pattern.search(response.text)
    if not match:
        print(f"{Fore.RED}[Error]{Style.RESET_ALL} Vulnerability data not found for IP {ip}.")
        return None

    vulns_data = json.loads(match.group(1))
    output_data = {"ip": ip, "vulnerabilities": {}}
    print(f"{Fore.YELLOW}Vulnerabilities found for {ip}:\n{Style.RESET_ALL}")

    for cve_id, details in vulns_data.items():
        summary = details.get("summary", "No summary available.")
        cvss = details.get("cvss", "N/A")
        ports = ", ".join(map(str, details.get("ports", [])))

        print(f"{Fore.GREEN}{Style.BRIGHT}CVE: {cve_id}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Summary:{Style.RESET_ALL} {summary}")
        print(f"{Fore.MAGENTA}CVSS Score:{Style.RESET_ALL} {cvss}")
        print(f"{Fore.BLUE}Affected Ports:{Style.RESET_ALL} {ports}\n")

        output_data["vulnerabilities"][cve_id] = {
            "summary": summary,
            "cvss": cvss,
            "ports": details.get("ports", [])
        }

    output_filename = f"{ip}.json"
    with open(output_filename, "w") as json_file:
        json.dump(output_data, json_file, indent=4)

    print(f"{Fore.YELLOW}[+] Results saved to {output_filename}{Style.RESET_ALL}")
    return output_filename

def get_ip_input():
    return input(">>Enter target IP: ")
