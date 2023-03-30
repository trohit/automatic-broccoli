#!/usr/bin/python3
def get_my_public_ip():
  r = requests.get("https://checkip.amazon.com")
  print(r.text)   
