from pwn import *

p = remote("34.170.146.252", 10790)

candidates = []
flag_length = 0

# 1回目の暗号文を取得して、フラグの長さを特定する
p.sendlineafter(b"Press Enter to get the encrypted flag...", b"")
p.recvuntil(b"Encrypted flag: ")
first_cipher = bytes.fromhex(p.recvline().strip().decode())
flag_length = len(first_cipher)

# 候補リストの初期化（長さ分だけ、0~255のセットを用意）
candidates = [set(range(256)) for _ in range(flag_length)]

log.info(f"Flag length detected: {flag_length}")
log.info("Starting exclusion attack. This may take a few seconds...")

iteration = 0
while True:
    # 現在の暗号文の各バイトを見て、候補から除外（削除）する
    for i, byte_val in enumerate(first_cipher):
        if byte_val in candidates[i]:
            candidates[i].remove(byte_val)

    # 全ての位置で候補が残り1つになったら終了
    if all(len(c) == 1 for c in candidates):
        break

    # 次の暗号文を取得
    iteration += 1
    p.sendlineafter(b"Press Enter to get the encrypted flag...", b"")
    p.recvuntil(b"Encrypted flag: ")
    first_cipher = bytes.fromhex(p.recvline().strip().decode())

    # 進行状況の表示 (500回ごと)
    if iteration % 500 == 0:
        log.info(f"Iteration {iteration}... narrowing down candidates.")

# 最後に残った1つの値を集めてフラグを復元
flag = bytes([list(c)[0] for c in candidates])

log.success(f"Flag found in {iteration} iterations!")
print(f"\n=> {flag.decode()}")
