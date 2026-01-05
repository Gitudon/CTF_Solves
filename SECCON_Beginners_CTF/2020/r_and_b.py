# coding: utf-8
# 2020/05/24 @HirMtsd
# Code for 'SECCON Beginners CTF 2020'

import codecs
import base64


# シーザ暗号復号
def rot13_(s):
    return codecs.decode(s, "rot13")


# Base64復号
def base64_(s):
    return (base64.b64decode(s.encode())).decode()


# 符号化データ
enc = "BQlVrOUllRGxXY2xGNVJuQjRkVFZ5U0VVMGNVZEpiRVpTZVZadmQwOWhTVEIxTkhKTFNWSkdWRUZIUlRGWFUwRklUVlpJTVhGc1NFaDFaVVY1Ukd0Rk1qbDFSM3BuVjFwNGVXVkdWWEZYU0RCTldFZ3dRVmR5VVZOTGNGSjFTMjR6VjBWSE1rMVRXak5KV1hCTGVYZEplR3BzY0VsamJFaGhlV0pGUjFOUFNEQk5Wa1pIVFZaYVVqRm9TbUZqWVhKU2NVaElNM0ZTY25kSU1VWlJUMkZJVWsxV1NESjFhVnBVY0d0R1NIVXhUVEJ4TmsweFYyeEdNVUUxUlRCNVIwa3djVmRNYlVGclJUQXhURVZIVGpWR1ZVOVpja2x4UVZwVVFURkZVblZYYmxOaWFrRktTVlJJWVhsTFJFbFhRVUY0UlZkSk1YRlRiMGcwTlE9PQ=="

# ループ
while True:
    print(enc)
    if not (enc[0] == "B" or enc[0] == "R"):
        break
    else:
        if enc[0] == "B":
            enc = base64_(enc[1:])
        elif enc[0] == "R":
            enc = rot13_(enc[1:])

print("FLAG:")
print(enc)
