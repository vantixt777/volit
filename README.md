 ![Image Alt](https://github.com/vantixt777/volit/blob/989e72005b6628974f90a9eabbf426ec254ba1d0/volit-pic.jpg)


### **1. Find Email Addresses (Option 1)**
- **What it does**: The tool generates possible email addresses based on the first name and optional last name you provide.
- **How it works**:
  - You enter a first name and optionally a last name.
  - The tool combines the name with common email domains (e.g., `gmail.com`, `yahoo.com`) and creates possible email addresses.
  - It uses various name formats (e.g., `firstname.lastname`, `firstname_lastname`, `firstname123`).
- **Example**:
  - Input: First name = `john`, Last name = `doe`
  - Output: `john.doe@gmail.com`, `john_doe@yahoo.com`, `john123@outlook.com`, etc.

---

### **2. Get IP Information (Option 2)**
- **What it does**: The tool retrieves detailed information about an IP address.
- **How it works**:
  - You enter an IP address (e.g., `46.167.63.139`).
  - The tool uses the `ip-api.com` API to fetch details like country, region, city, ISP, organization, latitude, longitude, timezone, and more.
- **Example**:
  - Input: IP = `46.167.63.139`
  - Output: Country = `Germany`, City = `Berlin`, ISP = `Deutsche Telekom`, etc.

---

### **3. Get Phone Number Information (Option 3)**
- **What it does**: The tool analyzes a phone number and provides information such as location, carrier, and timezone.
- **How it works**:
  - You enter a phone number (e.g., `+49123456789`).
  - The tool uses the `phonenumbers` library to parse and analyze the number.
- **Example**:
  - Input: Phone number = `+49123456789`
  - Output: Location = `Germany`, Carrier = `Deutsche Telekom`, Timezone = `Europe/Berlin`.

---

### **4. Port Scanning (Option 4)**
- **What it does**: The tool scans an IP address for open ports.
- **How it works**:
  - You enter an IP address.
  - The tool checks which ports in the range 1–1024 are open.
  - It uses multithreading to speed up the scanning process.
- **Example**:
  - Input: IP = `192.168.1.1`
  - Output: `Port 80 is open`, `Port 22 is open`, etc.

---

### **5. Username Checker (Option 5)**
- **What it does**: The tool checks if a specific username is available on various platforms.
- **How it works**:
  - You enter a username (e.g., `johndoe`).
  - The tool checks the availability on platforms like GitHub, Twitter, Instagram, Reddit, YouTube, Twitch, etc.
  - It sends an HTTP request to the platform and checks the status code (200 = username taken, 404 = username available).
- **Example**:
  - Input: Username = `johndoe`
  - Output: `[X] GitHub: https://github.com/johndoe (Username taken)`, `[✓] Twitter: https://twitter.com/johndoe (Username available)`.

---

### **6. MAC Address Lookup (Option 6)**
- **What it does**: This feature is not yet implemented but could be used to identify the manufacturer of a MAC address.
- **How it works**:
  - It would use an API like `macvendors.com` to fetch the manufacturer details.

---

### **7. Reverse IP Lookup (Option 7)**
- **What it does**: The tool finds all domains associated with a specific IP address.
- **How it works**:
  - You enter an IP address.
  - The tool uses the `hackertarget.com` API to retrieve a list of domains hosted on that IP.
- **Example**:
  - Input: IP = `46.167.63.139`
  - Output: `example.com`, `example2.com`, etc.

---

### **8. WHOIS Lookup (Option 8)**
- **What it does**: The tool retrieves WHOIS information for a domain.
- **How it works**:
  - You enter a domain (e.g., `example.com`).
  - The tool uses the `whois` library to fetch details like registration date, expiration date, registrar, and contact information.
- **Example**:
  - Input: Domain = `example.com`
  - Output: Registration date = `2020-01-01`, Registrar = `GoDaddy`, etc.

---

### **Additional Features**
- **Banner and Menu**:
  - The tool displays a colorful banner and a menu listing all available options.
- **Error Handling**:
  - The tool catches errors and displays user-friendly messages if something goes wrong (e.g., invalid input or network errors).
- **Colorful Output**:
  - The output is color-coded for better readability (green = success, red = error, yellow = warning).

---

### **Summary**
This tool is a versatile utility that offers the following features:
1. Generate email addresses.
2. Retrieve IP information.
3. Analyze phone numbers.
4. Scan for open ports.
5. Check username availability across multiple platforms.
6. Perform reverse IP lookups.
7. Fetch WHOIS information.

It’s ideal for security analysis, research, or general information gathering. 😊

---

If you have any questions or want to add more features, let me know! 🚀
