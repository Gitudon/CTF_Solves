cts = [
    238,
    55,
    26,
    13,
    30,
    30,
    21,
    56,
    58,
    43,
    60,
    40,
    52,
    45,
    6,
    47,
    48,
    33,
    53,
    51,
    62,
    24,
    37,
    61,
    5,
    56,
    7,
    23,
    83,
    123,
    44,
    56,
    52,
    24,
    7,
    23,
    15,
]


def decode_rot13_char(c):
    if "a" <= c <= "z":
        return chr((ord(c) - ord("a") - 13) % 26 + ord("a"))
    if "A" <= c <= "Z":
        return chr((ord(c) - ord("A") - 13) % 26 + ord("A"))
    return c


for key in range(256):
    pt = []
    for i in range(len(cts)):
        if i == 0:
            pt.append(cts[0] ^ key)
        else:
            pt.append(cts[i] ^ pt[i - 1])
    flag = "".join(decode_rot13_char(chr(c)) for c in pt)
    if flag.startswith("Alpaca{") and flag.endswith("}"):
        print(flag)
