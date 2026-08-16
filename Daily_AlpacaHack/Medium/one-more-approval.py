# https://github.com/kurimochi/ctf-writeups/blob/main/DailyAlpacaHack/202607/28_one-more-approval.md

from pwn import *

N = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551

HOST = "34.170.146.252"
PORT = 40280
conn = remote(HOST, PORT)

sig = bytearray.fromhex(conn.recvline().decode()[:-1])

s = int.from_bytes(sig[32:])
s = N - s

sig[32:] = int.to_bytes(s, 32)
conn.recvuntil(b"signature: ")
conn.sendline(sig.hex().encode())

flag = conn.recvline().decode()[:-1]
print(flag)
