# https://github.com/baumroll0928-spec/myRepository/tree/main/Daily_AlpacaHack/m202608/d03-04_Long_Long_Flag_Printer_2026

from pwn import *

HOST, PORT = "34.170.146.252", 36622
p = remote(HOST, PORT)

flag = b""
while len(flag) < 1024:
    d = p.recv(timeout=0.1)
    print(f"{d = }")
    flag += d
    time.sleep(0.1)
    # Ctrl + Cでサーバ側のsleepを解除する
    p.send(b"\x03")

print(flag)
