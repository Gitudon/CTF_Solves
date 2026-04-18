from pwn import *

p = remote("34.170.146.252", 29127)

# 復元用のバッファを用意
recovered_flag = b""

print("データを収集しています...")

for i in range(100):
    # "Press Enter..." のメッセージを待ってEnterを送信
    p.recvuntil(b"Press Enter to get the encrypted flag...")
    p.sendline()
    # "Encrypted flag: " の後ろの16進数文字列を取得
    p.recvuntil(b"Encrypted flag: ")
    cipher_hex = p.recvline().strip().decode()
    cipher_bytes = bytes.fromhex(cipher_hex)
    # 最初の1回目は recovered_flag にそのままコピー
    if len(recovered_flag) == 0:
        recovered_flag = bytearray(cipher_bytes)
    else:
        # 2回目以降は、各バイトごとにOR 演算をしてビットを埋めていく
        for j in range(len(cipher_bytes)):
            recovered_flag[j] |= cipher_bytes[j]
    # 進捗を表示
    print(
        f"\r[*] 試行回数: {i+1}/100  現在の状態: {recovered_flag}", end="", flush=True
    )

print("\n\n復元完了！")
print(recovered_flag.decode(errors="ignore"))

p.close()
