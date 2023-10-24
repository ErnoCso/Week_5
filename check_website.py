import sys
import requests

def check_website(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <URL>")
    else:
        url = sys.argv[1]
        is_working = check_website(url)
        
        if is_working:
            print(f"The website at {url} is working.")
        else:
            print(f"The website at {url} is not working or does not exist.")
			

#pip install requests
#python check_website.py http://example.com