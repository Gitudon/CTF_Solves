import sys
import copy

# 暗号化されたデータ
cipher = [
    4396,
    22819,
    47998,
    47995,
    40007,
    9235,
    21625,
    25006,
    4397,
    51534,
    46680,
    44129,
    38055,
    18513,
    24368,
    38451,
    46240,
    20758,
    37257,
    40830,
    25293,
    38845,
    22503,
    44535,
    22210,
    39632,
    38046,
    43687,
    48413,
    47525,
    23718,
    51567,
    23115,
    42461,
    26272,
    28933,
    23726,
    48845,
    21924,
    46225,
    20488,
    27579,
    21636,
]

ordered_cipher = copy.copy(cipher)

# 元の並び順の復元
for i in range(len(cipher)):
    c = cipher[i]
    for j in range(len(cipher)):
        if int(pow(c - j, 1 / 2)) ** 2 == c - j:
            ordered_cipher[j] = c - j
            break
cipher = ordered_cipher

flag = b"c"
for i in range(len(cipher)):
    m_i = flag[i]
    for j in range(0x20, 0x7F):
        c = (m_i + j) ** 2
        if c == cipher[i]:
            flag += chr(j).encode()
            break
        if j == 0x7E:
            print("not found", file=sys.stderr)
            sys.exit(1)
    print(flag)
