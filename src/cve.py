import requests
import json
import os
from colorama import Fore, Style
from config.config import URL

def get_cve_info(cve_id):
    url = f"{URL}/{cve_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

        filename = f"{cve_id}.json"
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"{Fore.GREEN}Output saved to:{Style.RESET_ALL} {Fore.YELLOW}{os.path.abspath(filename)}{Style.RESET_ALL}")

        summary = data.get("summary", "No summary available.")
        cvss_score = data.get("cvss_v3", "N/A")
        published_time = data.get("published_time", "N/A")
        references = data.get("references", [])
        epss = data.get("epss", "N/A")
        
        print(f"{Fore.GREEN}CVE ID:{Style.RESET_ALL} {Fore.YELLOW}{data['cve_id']}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Summary:{Style.RESET_ALL} {Fore.CYAN}{summary}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}CVSS Score (v3):{Style.RESET_ALL} {Fore.MAGENTA}{cvss_score}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Published Time:{Style.RESET_ALL} {Fore.BLUE}{published_time}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}EPSS:{Style.RESET_ALL} {Fore.RED}{epss}{Style.RESET_ALL}")

        if references:
            print(f"{Fore.GREEN}References:{Style.RESET_ALL}")
            for ref in references:
                print(f"{Fore.BLUE}- {ref}{Style.RESET_ALL}")

    except requests.exceptions.HTTPError as http_err:
        print(f"{Fore.RED}HTTP error occurred: {http_err}{Style.RESET_ALL}")
    except requests.exceptions.RequestException as req_err:
        print(f"{Fore.RED}Request error occurred: {req_err}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

def get_cve_input():
    return input(">>Enter CVE ID (Example:CVE-2024-6387): ")
