import socket
from termcolor import colored

def domain_to_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(colored(f"[•] Domain: {domain} -> IP Address: {ip_address}", 'green'))
        return ip_address
    except socket.gaierror:
        print(colored(f"[×] Unable to resolve domain: {domain}. Please check the domain name.", 'red'))
        return None

def domaintoip():
    print(colored("Domain to IP Address Converter", 'cyan', attrs=['bold']))
    print(colored("=" * 35, 'cyan', attrs=['bold']))

    domain = input(colored("Enter the domain name (e.g., example.com): ", 'yellow'))
    domain_to_ip(domain)

if __name__ == "__main__":
    domaintoip()
