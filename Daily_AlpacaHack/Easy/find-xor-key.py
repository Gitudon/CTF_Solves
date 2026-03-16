from itertools import cycle

c = bytes.fromhex(
    "031b13072d280a2c1816392f3b041d07020d2f1619232817153b24141d000c3925281a3704161b"
)

first_seven_bytes = c[:7]
key = bytes([c1 ^ c2 for c1, c2 in zip(first_seven_bytes, b"Alpaca{")])
print("Key:", key.decode())

flag = bytes([c1 ^ c2 for c1, c2 in zip(c, cycle(key))])

print("Flag:", flag.decode())
