# https://github.com/baumroll0928-spec/myRepository/tree/main/Daily_AlpacaHack/m202608/d05_Happy_Birthday

from hashlib import sha256


def H(m):
    return sha256(m).digest()[:5]


a_string = "user="
b_string = "admin="

a_dict = {}
for i in range(10**6):
    a = f"{a_string}{i}".encode()
    a_dict[H(a)] = a

i = 0
while True:
    b = f"{b_string}{i}".encode()
    hash_value = H(b)
    if hash_value in a_dict:
        a = a_dict[hash_value]
        print(a.hex())
        print(b.hex())
        break
    i += 1
