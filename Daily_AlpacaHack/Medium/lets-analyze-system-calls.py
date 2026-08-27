import time
from pwn import *

HOST, PORT = "34.170.146.252", 19291

val = 100

while val < 1024:
    time.sleep(0.5)
    p = remote(HOST, PORT)
    statement = p.recvline().decode()
    print(statement)
    result_1 = statement[10:]
    print(result_1)
    ans = val + int(result_1)
    print(ans)
    p.sendline(str(ans).encode())
    answer = p.recvline().decode()
    print(answer)
    if "Alpaca{" in answer:
        break
    p.close()
    val += 1
