from pwn import *
from Crypto.Hash.Poly1305 import Poly1305_MAC

io = remote("34.170.146.252", 12581)

# 1. サーバーからrを受け取る
io.recvuntil(b"HINT! r: ")
r_hex = io.recvline().strip().decode()
r = bytes.fromhex(r_hex)
print(f"[+] Received r: {r_hex}")

# 2. 任意のダミーメッセージを送信
dummy_message = b"hello"
io.sendlineafter(b"message: ", dummy_message)

# 3. サーバーから本物のタグを受け取る
real_tag_hex = io.recvline().strip().decode()
real_tag_bytes = bytes.fromhex(real_tag_hex)
print(f"[+] Received real tag: {real_tag_hex}")

# 4. 手元でs=0の時のタグを計算
zero_s = b"\x00" * 16
mac_zero = Poly1305_MAC(r, zero_s, dummy_message)
zero_tag_bytes = mac_zero.digest()

# 5. リトルエンディアンの整数として引き算し、sを復元
real_tag_int = int.from_bytes(real_tag_bytes, byteorder="little")
zero_tag_int = int.from_bytes(zero_tag_bytes, byteorder="little")

s_int = (real_tag_int - zero_tag_int) % (2**128)
s = s_int.to_bytes(16, byteorder="little")
print(f"[+] Recovered s: {s.hex()}")

# 6. 復元したsを使ってTARGETのタグを偽造
TARGET = b"admin=true"
mac_target = Poly1305_MAC(r, s, TARGET)
target_tag_hex = mac_target.hexdigest()
print(f"[+] Forged target tag: {target_tag_hex}")

# 7. 偽造したタグを送信してフラグを獲得
io.sendlineafter(b"tag: ", target_tag_hex.encode())

# フラグの出力を表示
print(io.recvall().decode().strip())
