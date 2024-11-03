import requests
import re
import json
from colorama import Fore, Style, init
from config.config import BASE_URL, HEADERS

init(autoreset=True)

def fetch_open_ports(ip):
    url = f"{BASE_URL}/{ip}"

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[Error]{Style.RESET_ALL} Could not retrieve data: {e}")
        return None

    ports_pattern = re.compile(r'<meta name="twitter:description" content="Ports open: (.*?)"/>')

    match_ports = ports_pattern.search(response.text)
    if match_ports:
        open_ports = match_ports.group(1).split(", ")
        print(f"{Fore.YELLOW}Open Ports for {ip}:{Style.RESET_ALL} {', '.join(open_ports)}")

        output_data = {"ip": ip, "open_ports": open_ports}
        output_filename = f"{ip}_port.json"
        with open(output_filename, "w") as json_file:
            json.dump(output_data, json_file, indent=4)

        print(f"{Fore.GREEN}[+] Results saved to {output_filename}{Style.RESET_ALL}")
        return output_filename
    else:
        print(f"{Fore.RED}[Error]{Style.RESET_ALL} Open ports data not found for IP {ip}.")
        return None

def get_ip_input():
    return input(">> Enter target IP: ")
