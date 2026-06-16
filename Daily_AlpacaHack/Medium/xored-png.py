# 1. 暗号化されたPNGファイルを読み込む
with open("flag.png.xored", "rb") as f:
    cipher_png = f.read()

# 2. 世界共通の「PNGの先頭16バイト」を定義
# (PNGマジックナンバー + IHDRチャンクの固定情報)
known_png_header = bytes(
    [
        0x89,
        0x50,
        0x4E,
        0x47,
        0x0D,
        0x0A,
        0x1A,
        0x0A,
        0x00,
        0x00,
        0x00,
        0x0D,
        0x49,
        0x48,
        0x44,
        0x52,
    ]
)

# 3. 暗号文の先頭16バイトと既知のヘッダをXORして、16バイトの鍵を逆算する
key = bytes([cipher_png[i] ^ known_png_header[i] for i in range(16)])
print(f"Key: {key.hex()}")

# 4. 判明した鍵を使ってファイル全体をもう一度XOR
decrypted_png = bytearray(cipher_png)
for i in range(len(decrypted_png)):
    decrypted_png[i] ^= key[i % len(key)]

# 5. 復元された本物のPNG画像を出力
with open("flag.png", "wb") as f_out:
    f_out.write(decrypted_png)
