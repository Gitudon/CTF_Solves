from pwn import *

io = remote("34.170.146.252", 48683)

received_line = io.recvline().strip().decode()

secret = received_line.split()[3]

# secretを改行なしで送り、送信を終了する
io.send(secret.encode())
io.shutdown("send")

print(io.recvall().decode())
