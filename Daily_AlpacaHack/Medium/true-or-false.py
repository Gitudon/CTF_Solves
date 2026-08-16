# https://github.com/baumroll0928-spec/myRepository/tree/main/Daily_AlpacaHack/m202607/d23_True_or_False

import pwn

HOST, PORT = "34.170.146.252", 20817
p = pwn.remote(HOST, PORT)

ans = 0
for i in range(28):
    code = f"2//(a//(3**{i})-3*(a//(3**{i+1})))==1"
    print(f"{code = }")
    p.sendlineafter(b"Eval > ", code.encode())
    res = p.recvline().strip()
    print(f"{res = }")
    if res == b"True":
        ans += 2 * (3**i)
    elif res == b"False":
        ans += 3**i

print(f"{ans = }")
p.sendlineafter(b"Guess > ", str(ans).encode())
print(p.recvline())
