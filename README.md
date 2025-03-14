# SubZeroEnum

SubZeroEnum is a Python-based subdomain enumeration tool designed to identify valid subdomains of a given domain using a wordlist. It checks for wildcard DNS records and verifies live subdomains by checking their HTTP response status.

## Installation and Usage

### Prerequisites

- **Linux OS** (Ubuntu, Debian, Kali, etc.)
- **Python 3** installed
- **Git** installed

### Installation

1. **Install Required Dependencies:**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip git figlet lolcat -y
   ```

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/daniyalusman/SubZeroEnum.git
   ```

3. **Navigate to the Directory:**
   ```bash
   cd SubZeroEnum
   ```

4. **Install Python Dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

### Usage

1. **Run the Script:**
   ```bash
   python3 subzeroenum.py
   ```

2. **Enter the target domain when prompted.**

3. **The tool will check for valid subdomains and save the results in a file named `<domain>.txt`.**

### Example

```bash
python3 subzeroenum.py
Enter domain: example.com
```

If valid subdomains are found, they will be saved in `example.com.txt` with their corresponding IP addresses.

## Features

- Uses a wordlist for subdomain enumeration
- Detects wildcard DNS records
- Checks HTTP status codes to verify live subdomains
- Saves results to a text file

## Notes

- Ensure you have a valid wordlist named `wordlist.txt` in the script directory.
- The script uses Google's (8.8.8.8) and Cloudflare's (1.1.1.1) DNS resolvers for querying subdomains.
- If you encounter installation issues, manually install missing dependencies using `sudo apt install <package-name>`.

## Author

**Daniyal Usman** - [GitHub](https://github.com/daniyalusman)

