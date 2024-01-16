#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
print(
    "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
    .format(type(the_page), the_page, the_page.decode())
)
