encrypted_msg = "aa9054e15ee209d458784a70bab6a5d62523f26eef2458cb3d48ccc6122fba1d75733c17c70a908a64b45b0caaf8d0e3bd30bcc0900283af88d82d4020cdacf7eaa5685ccf443776b4d9"
encrypted_flag = "af9d4dec44a333d44d2e0e62ade1f5c95a38e438eb6a0acf0b10c1b92513cf627828250ff43cbbae42db6244a3"
original_msg = (
    b"Daily AlpacaHack is a daily CTF challenge with a fun new puzzle every day."
)


def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)


def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))


# original_msg XOR keystream = encrypted_msg
# →keystream = encrypted_msg XOR original_msg
enc_msg_bytes = hex_to_bytes(encrypted_msg)
keystream = xor_bytes(enc_msg_bytes, original_msg)
enc_flag_bytes = hex_to_bytes(encrypted_flag)
decrypted_flag = xor_bytes(enc_flag_bytes, keystream)
print(decrypted_flag.decode())
