from pwn import *

HOST = "34.170.146.252"
PORT = 26148

io = remote(HOST, PORT)

# 1. 最初に出力される暗号化フラグを取得
io.recvuntil(b"encrypted flag = ")
enc_flag_hex = io.recvline().strip().decode()
enc_flag = bytes.fromhex(enc_flag_hex)
L = len(enc_flag)
N = (L + 15) // 16  # フラグが占めるブロック数

log.info(f"flag length = {L} bytes, blocks = {N}")

# 2. カウンタを 2^64 - N にセット(ラップアラウンドでブロック0に戻るようにする)
CNT = (1 << 64) - N

io.recvuntil(b"select> ")
io.sendline(b"2")
io.recvuntil(b"counter(dec)> ")
io.sendline(str(CNT).encode())
io.recvline()  # "Counter has been set."

# 3. ゼロ埋めの平文を 2*N ブロック分暗号化させる
#    最初のNブロックはジャンク(counter = 2^64-N ... 2^64-1)
#    次のNブロックは counter = 0 ... N-1 となり、enc_flagと同じkeystream
total_blocks = 2 * N
plaintext = b"\x00" * (16 * total_blocks)

io.recvuntil(b"select> ")
io.sendline(b"1")
io.recvuntil(b"plaintext(hex)> ")
io.sendline(plaintext.hex().encode())

io.recvuntil(b"encrypted text = ")
enc_hex = io.recvline().strip().decode()
enc = bytes.fromhex(enc_hex)

# 4. 後半Nブロックがkeystream(平文が0なので暗号文=keystream)
keystream = enc[16 * N : 16 * N + 16 * N]

flag = bytes(a ^ b for a, b in zip(enc_flag, keystream[:L]))
log.success(f"FLAG = {flag}")

io.recvuntil(b"select> ")
io.sendline(b"0")
io.close()
