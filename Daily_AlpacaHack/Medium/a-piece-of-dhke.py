from pwn import *
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad

HOST = "34.170.146.252"
PORT = 50224

g = 2
p_hex = """
FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1 29024E08 8A67CC74
020BBEA6 3B139B22 514A0879 8E3404DD EF9519B3 CD3CB093 FFFFFFFF FFFFFFFF
"""
p = int.from_bytes(bytes.fromhex(p_hex), "big")

h = pow(g, (p - 1) // 3, p)


def hash_int(x: int) -> bytes:
    x_bytes = long_to_bytes(x)
    return SHA256.new(x_bytes).digest()


def decrypt(key: int, data: bytes) -> bytes:
    iv, ciphertext = data[: AES.block_size], data[AES.block_size :]
    cipher = AES.new(key=hash_int(key), mode=AES.MODE_CBC, iv=iv)
    payload = cipher.decrypt(ciphertext)
    return unpad(payload, AES.block_size)


def main():
    print(f"[*] Connecting to {HOST}:{PORT}...")
    io = remote(HOST, PORT)
    io.recvuntil(b"ga = ")
    ga_val = io.recvline().strip().decode()
    print(f"[*] Server ga: {ga_val}")
    io.recvuntil(b"gb = ")
    io.sendline(str(h).encode())
    print(f"[+] Sent malicious gb (h): {h}")
    io.recvuntil(b"flag_enc = ")
    flag_enc_hex = io.recvline().strip().decode()
    print(f"[*] Received flag_enc: {flag_enc_hex}")
    flag_enc = bytes.fromhex(flag_enc_hex)
    possible_keys = [1, h, pow(h, 2, p)]
    print("[*] Crack testing with 3 possible keys...")
    for k in possible_keys:
        try:
            decrypted = decrypt(k, flag_enc)
            if b"Alpaca{" in decrypted:
                print("\n" + "=" * 40)
                print(f"[+] 攻略成功！ Flag: {decrypted.decode()}")
                print("=" * 40)
                break
        except Exception:
            continue
    io.close()


if __name__ == "__main__":
    main()
