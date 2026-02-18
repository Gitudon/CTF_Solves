from Crypto.Util.number import long_to_bytes
from functools import reduce

primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
    317,
    331,
    337,
    347,
    349,
]

out = [
    1,
    2,
    0,
    4,
    8,
    9,
    8,
    13,
    16,
    27,
    0,
    17,
    17,
    28,
    20,
    6,
    28,
    4,
    47,
    30,
    37,
    56,
    57,
    77,
    35,
    57,
    89,
    70,
    27,
    26,
    108,
    124,
    25,
    75,
    122,
    54,
    64,
    42,
    158,
    25,
    68,
    90,
    89,
    42,
    90,
    147,
    124,
    148,
    225,
    50,
    182,
    5,
    162,
    159,
    252,
    129,
    145,
    24,
    119,
    41,
    215,
    264,
    299,
    51,
    203,
    24,
    18,
    38,
    55,
    266,
]


def chinese_remainder(n, a):
    """
    n: 法のリスト (primes)
    a: 余りのリスト (out)
    """
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    """モジュロ逆元を計算"""
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


flag_long = chinese_remainder(primes, out)

print(long_to_bytes(flag_long).decode())
