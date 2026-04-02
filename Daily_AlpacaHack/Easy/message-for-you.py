import base64
import json
import zlib

# curl -c cookies.txt http://34.170.146.252:53703/
# ↑で取得したcookieの中からsessionの.で区切られた2番目の部分をコピーする
payload = "eJwlyzELwjAQhuG_cmRxcagUEbqJk6uDk3Cc5msNxlzJGaWU_ncjbi8PvLN7wkwGuM6d1GAkGZTh15d0Dhrx-ss1FlQ6rt6ge_AeiYT6KEO1X9bTgibqNdOkpaN9HOUm80GbxwbGklu2D9odS_K81QrgqSmLW77kUS59"
payload_decoded = base64.urlsafe_b64decode(payload + "===")
payload_json = json.loads(zlib.decompress(payload_decoded).decode())
print(json.dumps(payload_json, indent=4))
