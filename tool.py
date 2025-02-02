import requests
import whois
import json
import shodan

# Replace with your own API key
SHODAN_API_KEY = "MZJDs1EyjVqC7yspoOWvtCmKEKSeQUJi"

# Function to get WHOIS info
def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return {
            "Domain": w.domain_name,
            "Registrar": w.registrar,
            "Creation Date": str(w.creation_date),
            "Expiration Date": str(w.expiration_date),
            "Name Servers": w.name_servers
        }
    except Exception as e:
        return {"error": str(e)}

# Function to get IP info from Shodan
def get_shodan_info(ip):
    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        result = api.host(ip)
        return {
            "IP": result["ip_str"],
            "Organization": result.get("org", "N/A"),
            "Operating System": result.get("os", "N/A"),
            "Open Ports": result.get("ports", [])
        }
    except shodan.APIError as e:
        return {"error": str(e)}

# Function to run OSINT on a target
def osint_scan(target):
    results = {}

    # WHOIS Lookup
    if "." in target:  # Check if it's a domain
        results["WHOIS"] = get_whois_info(target)

    # Shodan Lookup (if input is an IP)
    if target.replace(".", "").isdigit():
        results["Shodan"] = get_shodan_info(target)

    return results

if __name__ == "__main__":
    target = input("Enter a domain or IP: ")
    report = osint_scan(target)

    # Save the report as a JSON file
    with open(f"{target}_osint_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print(f"OSINT report saved as {target}_osint_report.json")
