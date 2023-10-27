# Task 4

# Write a program that takes a URL as a command-line argument and reports
# whether or not there is a working website at that address.
# Hint: You need to get the HTTP response code.
# Another Hint: StackOverflow is your friend

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


if len(sys.argv) != 2:
    print("Usage: python check_website.py <URL>")
else:
    url = sys.argv[1]
    is_working = check_website(url)

    if is_working:
        print(f"The website at {url} is working.")
    else:
        print(f"The website at {url} is not working or does not exist.")


# pip install requests
# python check_website.py https://something.com
