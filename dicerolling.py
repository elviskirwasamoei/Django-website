from urllib.request import urlopen

response = urlopen("https://python.org")
response.read()