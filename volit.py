import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import socket
import threading
from colorama import init, Fore, Style
import os
from pystyle import Colors, Colorate
import smtplib
import dns.resolver
import time
import concurrent.futures
import whois

# Initialize color output
init(autoreset=True)

# Define colors
red = "\033[31m"
reset = "\033[0m"
yellow = "\033[93m"
green = "\033[92m"

# Function to print banner
def print_banner():
    os.system("clear" if os.name == "posix" else "cls")
    interface = """
 ▄█    █▄        ▄██████▄        ▄█             ▄█           ███     
███    ███      ███    ███      ███            ███       ▀█████████▄ 
███    ███      ███    ███      ███            ███▌         ▀███▀▀██ 
███    ███      ███    ███      ███            ███▌          ███   ▀ 
███    ███      ███    ███      ███            ███▌          ███     
███    ███      ███    ███      ███            ███           ███     
███    ███      ███    ███      ███▌    ▄      ███           ███     
 ▀██████▀        ▀██████▀       █████▄▄██      █▀           ▄████▀   
    """
    print(Colorate.Horizontal(Colors.blue_to_purple, interface))

# Function to print menu inside a box with the same color as the banner
def print_menu():
    menu = Colorate.Horizontal(Colors.blue_to_purple, """
╔══════════════════════════════╗
║          MENU OPTIONS        ║
╠══════════════════════════════╣
║ 1. Find Email                ║
║ 2. Get IP Information        ║
║ 3. Get Phone Number Info     ║
║ 4. Scan Ports                ║
║ 5. Check Username            ║
║ 6. Get MAC Address Info      ║
║ 7. Reverse IP Lookup         ║
║ 8. WHOIS Lookup              �
╚══════════════════════════════╝

           by vantixt
""")
    print(menu)

# Function to find email
def find_email():
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name (optional): ").strip().lower()
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "aol.com", "protonmail.com", "icloud.com", "zoho.com", "yandex.com", "gmx.com", "mail.com"]
    formats = [
        f"{first_name}.{last_name}", f"{first_name}{last_name}",
        f"{first_name}_{last_name}", f"{first_name[0]}{last_name}",
        f"{last_name}.{first_name}", f"{first_name}-{last_name}",
        f"{first_name}{last_name[0]}", f"{first_name[0]}_{last_name}"
    ] if last_name else [first_name, f"{first_name}123", f"{first_name}99"]
    
    emails = [f"{fmt}@{domain}" for fmt in formats for domain in domains]
    
    print(f"{green}Possible emails:{reset}")
    for email in emails:
        print(email)

# Function to get IP information
def get_ip_info(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        
        if data["status"] == "success":
            print(f"{green}IP Information for {ip}:{reset}")
            print(f"Country: {data.get('country', 'N/A')}")
            print(f"Region: {data.get('regionName', 'N/A')}")
            print(f"City: {data.get('city', 'N/A')}")
            print(f"ISP: {data.get('isp', 'N/A')}")
            print(f"Organization: {data.get('org', 'N/A')}")
            print(f"AS: {data.get('as', 'N/A')}")
            print(f"Latitude: {data.get('lat', 'N/A')}")
            print(f"Longitude: {data.get('lon', 'N/A')}")
            print(f"Timezone: {data.get('timezone', 'N/A')}")
            print(f"ZIP: {data.get('zip', 'N/A')}")
        else:
            print(f"{red}Failed to fetch IP information. Error: {data.get('message', 'Unknown error')}{reset}")
    except Exception as e:
        print(f"{red}Error fetching IP information: {e}{reset}")

# Function to get phone number information
def get_phone_info(phone):
    try:
        parsed_number = phonenumbers.parse(phone)
        location = geocoder.description_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)
        
        print(f"{green}Phone Number Information:{reset}")
        print(f"Location: {location}")
        print(f"Carrier: {carrier_name}")
        print(f"Time Zones: {', '.join(time_zones)}")
    except Exception as e:
        print(f"{red}Invalid phone number. Error: {e}{reset}")

# Function to scan ports
def scan_ports(ip, start_port=1, end_port=1024):
    print(f"Scanning {ip} from port {start_port} to {end_port}...")
    open_ports = []
    
    def scan(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((ip, port)) == 0:
                open_ports.append(port)
                print(f"{green}Port {port} is open{reset}")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(scan, range(start_port, end_port + 1))
    
    if not open_ports:
        print(f"{red}No open ports found.{reset}")

# Reverse IP Lookup
def reverse_ip_lookup(ip):
    url = f"https://api.hackertarget.com/reverseiplookup/?q={ip}"
    try:
        response = requests.get(url)
        print(f"{green}Domains associated with {ip}:{reset}\n{response.text}")
    except requests.RequestException as e:
        print(f"{red}Error: {e}{reset}")

# WHOIS Lookup
def whois_lookup(domain):
    try:
        info = whois.whois(domain)
        print(f"{green}WHOIS Info for {domain}:{reset}\n{info}")
    except Exception as e:
        print(f"{red}Error fetching WHOIS data: {e}{reset}")

# Function to check username availability
def check_username(username):
    websites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Reddit": f"https://reddit.com/user/{username}",
        "YouTube": f"https://youtube.com/{username}",
        "Twitch": f"https://twitch.tv/{username}",
        "Pinterest": f"https://pinterest.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Flickr": f"https://flickr.com/people/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "DeviantArt": f"https://{username}.deviantart.com",
        "VK": f"https://vk.com/{username}",
        "About.me": f"https://about.me/{username}",
        "Disqus": f"https://disqus.com/by/{username}",
        "Flipboard": f"https://flipboard.com/@{username}",
        "Slack": f"https://{username}.slack.com",
        "Goodreads": f"https://goodreads.com/{username}",
        "Patreon": f"https://patreon.com/{username}",
        "Bitbucket": f"https://bitbucket.org/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Keybase": f"https://keybase.io/{username}",
        "Codepen": f"https://codepen.io/{username}",
        "Behance": f"https://behance.net/{username}",
        "Foursquare": f"https://foursquare.com/{username}",
        "HubPages": f"https://hubpages.com/@{username}",
    }

    print(f"{green}Checking username availability for '{username}':{reset}")
    for site, url in websites.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{red}[X] {site}: {url} (Username taken){reset}")
            elif response.status_code == 404:
                print(f"{green}[✓] {site}: {url} (Username available){reset}")
            else:
                print(f"{yellow}[?] {site}: {url} (Status code: {response.status_code}){reset}")
        except requests.RequestException as e:
            print(f"{yellow}[?] {site}: {url} (Error: {e}){reset}")

# Main menu
def main():
    print_banner()
    print_menu()
    choice = input(f"{red}\nPlease select an option (1-8): {reset}")
    if choice == "1":
        find_email()
    elif choice == "2":
        ip = input("Enter IP address: ")
        get_ip_info(ip)
    elif choice == "3":
        phone = input("Enter phone number: ")
        get_phone_info(phone)
    elif choice == "4":
        ip = input("Enter IP address: ")
        scan_ports(ip)
    elif choice == "5":
        username = input("Enter username: ")
        check_username(username)
    elif choice == "6":
        mac = input("Enter MAC address: ")
        print("MAC address lookup feature not implemented yet.")
    elif choice == "7":
        ip = input("Enter IP address: ")
        reverse_ip_lookup(ip)
    elif choice == "8":
        domain = input("Enter domain: ")
        whois_lookup(domain)
    else:
        print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
