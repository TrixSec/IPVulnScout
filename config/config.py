import random
from termcolor import colored

BASE_URL = "https://www.shodan.io/host"
URL = "https://cvedb.shodan.io/cve"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

IPVULNSCOUT_VERSION = "1.0"
AUTHOR = "Trix Cyrus"
COPYRIGHT = "Copyright © 2024 Trixsec Org"

def print_banner():
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'] 
    random_color = random.choice(colors) 

    banner = r"""
██╗██████╗ ██╗   ██╗██╗   ██╗██╗     ███╗   ██╗███████╗ ██████╗ ██████╗ ██╗   ██╗████████╗
██║██╔══██╗██║   ██║██║   ██║██║     ████╗  ██║██╔════╝██╔════╝██╔═══██╗██║   ██║╚══██╔══╝
██║██████╔╝██║   ██║██║   ██║██║     ██╔██╗ ██║███████╗██║     ██║   ██║██║   ██║   ██║   
██║██╔═══╝ ╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║╚════██║██║     ██║   ██║██║   ██║   ██║   
██║██║      ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   
╚═╝╚═╝       ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   
    """
    print(colored(banner, random_color)) 
    print(colored(f"IPVulnScout Version: {IPVULNSCOUT_VERSION}", 'yellow'))
    print(colored(f"Made by {AUTHOR}", 'yellow'))
    print(colored(COPYRIGHT, 'green'))
    print("")
