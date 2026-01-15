from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# ここに表示されたkeyを入力
key_hex = input("Enter the key (hex): ")
key = bytes.fromhex(key_hex)

ALPACA = chr(129433)
target_plaintext = (ALPACA * 5).encode()

iv = b"0123456789abcdef"
cipher = AES.new(key, AES.MODE_CBC, iv)

padded_target = pad(target_plaintext, AES.block_size)
ciphertext = cipher.encrypt(padded_target)

# 以下の出力をサーバに入力するとフラグを獲得できる
print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"IV (hex): {iv.hex()}")
