from pwn import *

p = remote("34.170.146.252", 30351)

# PBOXの定義（問題文からコピー）
PBOX = [
    5,
    22,
    31,
    18,
    3,
    19,
    11,
    13,
    10,
    25,
    24,
    0,
    2,
    17,
    20,
    12,
    6,
    26,
    1,
    7,
    16,
    4,
    27,
    21,
    15,
    8,
    30,
    28,
    14,
    23,
    29,
    9,
]

# 1. 最初に表示される「暗号化されたCHALLENGE」を取得
p.recvuntil(b"CHALLENGE: ")
enc_challenge = bytes.fromhex(p.recvline().strip().decode())

# 2. すべてゼロの平文(32バイト)を送信してE(0)を取得
zero_pt = b"00" * 32
p.sendlineafter(b"pt: ", zero_pt)
e_zero = bytes.fromhex(p.recvline().strip().decode())

# 3. 暗号文とE(0)をXORして、Pboxで32回シャッフルされた状態の平文を取得
xored = bytes([a ^ b for a, b in zip(enc_challenge, e_zero)])

# 4. Pboxの逆変換（リバース）を32回行って、元の平文に戻す
pt = xored
for _ in range(32):
    orig = bytearray(32)
    # C[i] = P[PBOX[i]] なので、逆に代入していく
    for i in range(32):
        orig[PBOX[i]] = pt[i]
    pt = orig

recovered_challenge = pt
log.success(f"Recovered CHALLENGE: {recovered_challenge.hex()}")

# 5. "guess" モードに入り、復元したCHALLENGEを送信！
p.sendlineafter(b"pt: ", b"guess")
p.sendlineafter(b"challenge: ", recovered_challenge.hex().encode())

# 6. フラグを回収
p.recvuntil(b"flag: ")
flag = p.recvline().strip().decode()

print("\n=== FLAG ===")
print(flag)
