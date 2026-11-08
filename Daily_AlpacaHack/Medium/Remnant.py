# https://github.com/baumroll0928-spec/myRepository/tree/main/Daily_AlpacaHack/m202611/d02-04_Remnant

from base64 import b64decode
import pwn

HOST, PORT = "34.170.146.252", 35075
p = pwn.remote(HOST, PORT)


def is_error(pre: str, ch: str) -> bool:
    p.sendlineafter(b": ", (pre + ch).encode())
    d = p.recvline()
    return d.startswith(b"Err")


def find_next_char(pre: str) -> str:
    cnt = 0
    last_idx = -1
    if is_error(pre, " "):
        # アルファベット
        for i in range(1, 16):
            if not is_error(pre, chr(0x20 + i)):
                cnt += 1
                last_idx = i
        if cnt == 1:
            # 上段
            if is_error(pre, chr(0x4F ^ last_idx)):
                # 小文字(a-o)
                return chr(0x60 + last_idx)
            else:
                # 大文字(A-O)
                return chr(0x40 + last_idx)
        # 下段
        for i in range(11):
            if not is_error(pre, chr(0x30 + i)):
                last_idx = i
                break
        if is_error(pre, chr(0x5F - last_idx)):
            # 小文字(p-z)
            return chr(0x70 + last_idx)
        else:
            # 大文字(P-Z)
            return chr(0x50 + last_idx)
    else:
        # アルファベット以外
        for i in range(16):
            if not is_error(pre, chr(0x60 + i)):
                cnt += 1
                last_idx = i
        if cnt == 1:
            # 記号(+/)
            return chr(0x20 + last_idx)
        for i in range(10):
            if not is_error(pre, chr(0x70 + i)):
                # 数字(0-9)
                return chr(0x30 + i)
        # 記号(=)
        return "="


flag_b64 = "QWxwYWNhe"
for _ in range(7):
    flag_b64 += find_next_char(flag_b64)
    print(flag_b64)
flag = b64decode(flag_b64.encode()) + b"}"
print(f"{flag = }")
