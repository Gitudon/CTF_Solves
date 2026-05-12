enc = [
    0x31,
    0x54,
    0x6C,
    0x2F,
    0x04,
    0x52,
    0x22,
    0x41,
    0x3F,
    0x59,
    0x27,
    0x45,
    0x67,
    0x79,
    0x1A,
    0x4E,
    0x78,
    0x2D,
    0x19,
]


def step(s):
    # C言語の uint16_t を再現するために 0xFFFF でマスク
    bit = ((s >> 0) ^ (s >> 2) ^ (s >> 3) ^ (s >> 5)) & 1
    return ((s >> 1) | (bit << 15)) & 0xFFFF


state = 0xACE1
flag = ""

for i in range(len(enc)):
    state = step(state)
    # enc[i] と state の下位7ビットを XOR
    char_code = enc[i] ^ (state & 0x7F)
    flag += chr(char_code)

print(f"Flag: {flag}")
