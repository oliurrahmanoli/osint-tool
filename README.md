# 🔍 OSINT Data Gathering Tool


## 🛠️ About
**OSINT Data Gathering Tool** is an automated reconnaissance script that collects publicly available information about a target using:
- **WHOIS Lookup** 📌 (Domain registration details)
- **Shodan API** 🌐 (IP Intelligence)
- **Future Features**: Email and subdomain enumeration, social media tracking.

---

## 📌 Features
✅ WHOIS lookup for domain details  
✅ Shodan API integration for IP reconnaissance  
✅ Automatic JSON report generation  

---

## 🚀 Installation
1. **Clone the repo**
   
   git clone https://github.com/yourusername/osint-tool.git
   cd osint-tool
   
2.Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install dependencies
pip install -r requirements.txt


📂 Usage
Run the script and enter a domain or IP:
python osint_tool.py
Example:

Enter a domain or IP: example.com
OSINT report saved as example.com_osint_report.json
View the report:

cat example.com_osint_report.json

⚙️ Configuration
Before running the tool, update your Shodan API Key in osint_tool.py:
SHODAN_API_KEY = "your_shodan_api_key"


📌 Example Output

{
    "WHOIS": {
        "Domain": "example.com",
        "Registrar": "GoDaddy",
        "Creation Date": "1995-08-13",
        "Expiration Date": "2025-08-13",
        "Name Servers": ["ns1.example.com", "ns2.example.com"]
    },
    "Shodan": {
        "IP": "8.8.8.8",
        "Organization": "Google LLC",
        "Operating System": "N/A",
        "Open Ports": [80, 443]
    }
}
📌 Roadmap (Future Enhancements)

 ✅ Add email and subdomain reconnaissance using TheHarvester.
 ✅ Implement reverse DNS lookup.
 ✅ Support for Markdown reports.
 
👨‍💻 Author & Contact
Name: Oliur Rahman Oli
Portfolio: oliurrahman.tech
GitHub: @oliurrahmanoli


⚠️ Disclaimer
This tool is for educational purposes only. Use it responsibly!

⭐ Contribute & Support
If you like this project, give it a ⭐ star and share your feedback!

