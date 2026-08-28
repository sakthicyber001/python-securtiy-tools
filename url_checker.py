from urllib.parse import urlparse

url = input("Enter a URL: ")

parsed_url = urlparse(url)

if parsed_url.scheme in ["http", "https"] and parsed_url.netloc:
    print("Valid URL")
    print("Host:", parsed_url.netloc)
else:
    print("Invalid URL")
