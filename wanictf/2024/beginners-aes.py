from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
import hashlib

key_prefix = b"the_enc_key_is_"
iv_prefix = b"my_great_iv_is_"
enc = b'\x16\x97,\xa7\xfb_\xf3\x15.\x87jKRaF&"\xb6\xc4x\xf4.K\xd77j\xe5MLI_y\xd96\xf1$\xc5\xa3\x03\x990Q^\xc0\x17M2\x18'
target_hash = "6a96111d69e015a07e96dcd141d31e7fc81c4420dbbef75aef5201809093210e"

for key_byte in range(256):
    for iv_byte in range(256):
        key = key_prefix + bytes([key_byte])
        iv = iv_prefix + bytes([iv_byte])

        try:
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted_msg = unpad(cipher.decrypt(enc), 16)
            if hashlib.sha256(decrypted_msg).hexdigest() == target_hash:
                print(f"Success! Key: {key}, IV: {iv}")
                print(f"decrypted_msg = {decrypted_msg.decode()}")
                print(
                    f"decrypted_msg_hash = {hashlib.sha256(decrypted_msg).hexdigest()}"
                )
                break
        except (ValueError, KeyError):
            continue
    else:
        continue
    break

print("Finished trying all combinations.")
