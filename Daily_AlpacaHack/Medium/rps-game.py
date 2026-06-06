from pwn import *

io = remote("34.170.146.252", 45243)

# 最初はパーを出して様子を見る
io.recvuntil(b"Round 1 > ")
io.sendline(b"p")

for i in range(1, 1000):
    print(f"Round {i+1}")
    hand_data = io.recvuntil(b"Round ")
    # 相手が直前に出した手を特定する
    if b"Opponent: r" in hand_data:
        next_hand = b"p"  # 相手は次もグー(r)を出しやすいので、パー(p)を出す
    elif b"Opponent: p" in hand_data:
        next_hand = b"s"  # 相手は次もパー(p)を出しやすいので、チョキ(s)を出す
    elif b"Opponent: s" in hand_data:
        next_hand = b"r"  # 相手は次もチョキ(s)を出しやすいので、グー(r)を出す
    io.recvuntil(b"> ")
    io.sendline(next_hand)

print(io.recvall().decode())
