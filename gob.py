import sys
import requests

def gobuster(ip, wordlist_path):
    try:
        with open(wordlist_path, 'r') as wordlist_file:
            wordlist = wordlist_file.read().splitlines()

        for word in wordlist:
            url = f"http://{ip}/{word}"
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Found: {url}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 your_script.py <ip_address> <wordlist_path>")
        sys.exit(1)
    
    ip_address = sys.argv[1]
    wordlist_path = sys.argv[2]

    gobuster(ip_address, wordlist_path)

