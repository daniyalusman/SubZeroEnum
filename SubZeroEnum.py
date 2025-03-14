from dns import resolver
import requests
import os
import shutil

def install_package(package):
    if not shutil.which(package):
        print(f"[*] Installing {package}...")
        if os.system(f"sudo apt install {package} -y") != 0:
            print(f"[!] Error: Failed to install {package}. Please install it manually.")
            exit(1)

install_package("figlet")
install_package("lolcat")

lolcat_path = shutil.which("lolcat") or "/usr/games/lolcat"

if os.path.exists(lolcat_path):
    os.system(f"figlet 'SubZeroEnum' | {lolcat_path}")
else:
    print("[!] Error: lolcat not found. Please check your installation.")

print("\033[33m# Coded by Daniyal Usman - https://github.com/daniyalusman \033[0m\n")  

res = resolver.Resolver()
res.nameservers = ['8.8.8.8', '1.1.1.1'] 
res.timeout = 3
res.lifetime = 5

def is_wildcard(subdomain_ip, wild_card_ip):
    return subdomain_ip == wild_card_ip

def check_status_code(subdomain):
    try:
        r = requests.get(f"https://{subdomain}", timeout=5)
        return r.status_code
    except requests.exceptions.RequestException:
        try:
            r = requests.get(f"http://{subdomain}", timeout=5)
            return r.status_code
        except requests.exceptions.RequestException:
            return False 

def subdomain_enum(domain):
    try:
        res.resolve(domain, 'A')
    except resolver.NXDOMAIN:
        print(f"Error: The domain \"{domain}\" does not exist. Please enter a valid domain.")
        return

    random_subdomain = "3uxiw01." + domain
    try:
        wild_card_ip = str(res.resolve(random_subdomain, 'A')[0])
    except (resolver.NXDOMAIN, resolver.NoAnswer, resolver.NoNameservers, resolver.LifetimeTimeout):
        wild_card_ip = ''

    valid_subdomains = []
    output_file_name = domain + ".txt"

    with open(output_file_name, 'w') as output_file:
        with open('wordlist.txt', 'r') as wordlist:
            for word in wordlist:
                word = word.strip().strip(".")
                if not word:
                    continue
                subdomain = word + "." + domain

                if ".." in subdomain:
                    continue
                try:
                    print(f"Trying {subdomain}")
                    subdomain_ip = str(res.resolve(subdomain, 'A')[0])
                except (resolver.NXDOMAIN, resolver.NoAnswer, resolver.NoNameservers, resolver.LifetimeTimeout):
                    continue
                else:
                    if not is_wildcard(subdomain_ip, wild_card_ip):
                        if check_status_code(subdomain) == 200: 
                            if subdomain not in valid_subdomains:
                                valid_subdomains.append(f"{subdomain} --> {subdomain_ip}")
                                print(f"[+] Found {subdomain} --> {subdomain_ip}")
                                output_file.write(f"{subdomain} --> {subdomain_ip}\n")

    print("File saved successfully.")

try:
    target_domain = input("Enter domain: ")
    subdomain_enum(target_domain)
except KeyboardInterrupt:
    print("\n...\n")
