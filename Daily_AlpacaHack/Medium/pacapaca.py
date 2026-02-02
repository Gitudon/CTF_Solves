iv_old = bytes.fromhex("8b93e320ba9287a0ea8c82a9add5b1fc")
token = bytes.fromhex(
    "1a7e7ad6a90df5ca3f1b21cd0655e29b07f373ad9e61f2329148fa5a32a1fcb45cb1ae4390ae70fe6b7a8d37ec886f9d"
)

p_old = b'{"name": "alpaca'
p_new = b'{"name":  "llama'

xor_diff = bytes([a ^ b for a, b in zip(p_old, p_new)])
iv_new = bytes([a ^ b for a, b in zip(iv_old, xor_diff)])

print("New IV:", iv_new.hex())
