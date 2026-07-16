import requests

# Use only against domains you own or are authorized to test.
target_domain = "google.com"
wordlist_path = "/home/kali/Desktop/subdomains.txt"


def probe(hostname):
    try:
        response = requests.get(f"https://{hostname}", timeout=5)
        if response.status_code == 200:
            print(response, f"https://{hostname}")
    except requests.exceptions.ConnectionError:
        print("[-] Connection error", f"https://{hostname}")
    except requests.exceptions.Timeout:
        print("[-] Request timed out", f"https://{hostname}")


with open(wordlist_path, encoding="utf-8") as words_file:
    for line in words_file:
        subdomain = line.strip()
        if subdomain:
            probe(f"{subdomain}.{target_domain}")
