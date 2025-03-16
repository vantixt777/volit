import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import socket
import threading
from colorama import init, Fore, Style
import os

# Initialize color output
init(autoreset=True)

# Define colors
red = "\033[31m"
reset = "\033[0m"
yellow = "\033[93m"
green = "\033[92m"

# Function to get IP information
def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

# Function to get phone number information
def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if phonenumbers.is_valid_number(parsed_number):
            country = geocoder.description_for_number(parsed_number, "en")
            provider = carrier.name_for_number(parsed_number, "en")
            timezones = timezone.time_zones_for_number(parsed_number)

            phone_info_banner = f"""
{red}\033[1mPhone Number Info:{reset}
Phone Number: {phone_number}
  - Country: {country}
  - Carrier: {provider}
  - Timezones: {', '.join(timezones)}
"""
            print(phone_info_banner)
        else:
            print("Invalid phone number.")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Error parsing the phone number.")

# Function to get MAC address information
def get_mac_info(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The MAC address {mac_address} belongs to:")
            print(response.text)
        else:
            print(f"{red}[!] Error: No information found for MAC address {mac_address}.{reset}")
    except requests.exceptions.RequestException as e:
        print(f"{red}[!] Error fetching data: {e}{reset}")

# Username check
PLATFORMS = [
    'github.com', 'twitter.com', 'instagram.com', 'facebook.com', 'linkedin.com',
    'pinterest.com', 'twitch.tv', 'youtube.com', 'reddit.com', 'snapchat.com',
    'tumblr.com', 'steamcommunity.com', 'aniworld.com', 'discord.com', 'guns.lol'
]

def check_username_on_platform(username, platform):
    url = f'https://{platform}/{username}'
    response = requests.get(url)
    
    if response.status_code == 404:
        print(f'{green}[✔] {platform} - {username} is available! Link: {url}')
    elif response.status_code == 200:
        print(f'{red}[✘] {platform} - {username} is taken! Link: {url}')
    else:
        print(f'{yellow}[?] {platform} - Error checking username.')

def search_username(username):
    print(f'\nChecking username: {username}')
    
    for platform in PLATFORMS:
        check_username_on_platform(username, platform)

# Port scanner
def scan_port(ip, port, show_closed=False):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))

        if result == 0:
            print(Fore.GREEN + f"  [+] Port {port} is open ✅")
        elif show_closed:
            print(Fore.RED + f"  [-] Port {port} is closed ❌")

        sock.close()
    except socket.error as err:
        print(Fore.YELLOW + f"  [!] Error scanning port {port}: {err}")

def scan_ports(ip, start_port, end_port, show_closed=False):
    print(Fore.MAGENTA + f"📡 Scanning {ip} from port {start_port} to {end_port}...\n")
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port, show_closed))
        threads.append(thread)
        thread.start()
        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []

    for thread in threads:
        thread.join()

# Print banner
def print_banner():
    os.system("clear" if os.name == "posix" else "cls")  # Clear screen
    banner = f"""{red}\033[1m
 ▄█    █▄        ▄██████▄        ▄█             ▄█           ███     
███    ███      ███    ███      ███            ███       ▀█████████▄ 
███    ███      ███    ███      ███            ███▌         ▀███▀▀██ 
███    ███      ███    ███      ███            ███▌          ███   ▀ 
███    ███      ███    ███      ███            ███▌          ███     
███    ███      ███    ███      ███            ███           ███     
███    ███      ███    ███      ███▌    ▄      ███           ███     
 ▀██████▀        ▀██████▀       █████▄▄██      █▀           ▄████▀   
                                ▀                                        

    ╔════════════════════════════════════╗
    ║          [1] IP Scan               ║
    ║          [2] Username Scan         ║
    ║          [3] Phone Number Info     ║
    ║          [4] MAC Address Scan      ║
    ║          [5] Port Scanner          ║
    ╚════════════════════════════════════╝

              by vantixt
{reset}"""
    print(banner)

# Main menu
def main():
    print_banner()

    choice = input(f"{red}\nPlease select an option (1, 2, 3, 4, or 5): {reset}")

    if choice == "1":
        ip_address = input(f"{yellow}\nEnter an IP address: {reset}")
        ip_info = get_ip_info(ip_address)
        print(ip_info)

    elif choice == "2":
        username = input(f"{yellow}\nEnter a username: {reset}")
        search_username(username)

    elif choice == "3":
        phone_number = input(f"{yellow}\nEnter a phone number: {reset}")
        get_phone_info(phone_number)

    elif choice == "4":
        mac_address = input(f"{yellow}\nEnter a MAC address (XX:XX:XX:XX:XX:XX): {reset}")
        if len(mac_address) == 17 and mac_address.count(':') == 5:
            get_mac_info(mac_address)
        else:
            print(f"{red}[!] Invalid MAC address format.{reset}")

    elif choice == "5":
        target_ip = input(Fore.CYAN + "🌍 Enter the IP address: ")
        start_port = int(input(Fore.CYAN + "🔢 Start Port: "))
        end_port = int(input(Fore.CYAN + "🔢 End Port: "))
        show_closed = input(Fore.YELLOW + "👀 Show closed ports? (y/n): ").strip().lower() == 'y'
        scan_ports(target_ip, start_port, end_port, show_closed)
        print(Fore.CYAN + "\n✅ Scan completed.")

if __name__ == "__main__":
    main()
