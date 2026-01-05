from Crypto.Util.number import *
import base64

long_value = 373502670300504551747111047082539140193958649718
hex_string = "346c5f6833785f6630726d61745f31735f636c33"
base64_string = "NG5fYjY0X3A0ZGQxbmdfaXNfY29vbH0="

flag_part1 = long_to_bytes(long_value).decode()
flag_part2 = bytes.fromhex(hex_string).decode()
flag_part3 = base64.b64decode(base64_string).decode()

print(flag_part1 + flag_part2 + flag_part3)
