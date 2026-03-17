from pwn import *
from randcrack import RandCrack  # pip install pwntools randcrack


def solve():
    # サーバーに接続
    io = remote("34.170.146.252", 6911)
    rc = RandCrack()
    print("[*] 過去の乱数を624個収集し、内部状態をクローンします...")
    # 1. 624個の32bit乱数を取得してRandCrackに学習させる
    # それなりに時間がかかるので注意
    for _ in range(624):
        io.sendlineafter(b"> ", b"1")
        io.recvuntil(b"] ")
        val = int(io.recvline().strip())
        rc.submit(val)  # 状態を学習
    print("[+] 内部状態のクローンに成功しました！")
    # 2. 未来を予言するフェーズへ移行
    io.sendlineafter(b"> ", b"2")
    # 3. サーバーからスキップ回数(i)を読み取る
    io.recvuntil(b"timeline: i = ")
    skip_count = int(io.recvline().strip())
    print(f"[*] サーバーは乱数を {skip_count} 回スキップします。")
    # 4. 手元のクローンPRNGも同じ回数だけ空回しする
    for _ in range(skip_count):
        rc.predict_getrandbits(32)
    # 5. 次に出るはずの乱数を予測！
    predicted_ans = rc.predict_getrandbits(32)
    print(f"[+] 予測された未来の数値: {predicted_ans}")
    # 6. 予測した数値を送信
    io.sendlineafter(b"Speak the next omen > ", str(predicted_ans).encode())
    # 7. フラグを受け取って表示
    print(io.recvall().decode())


if __name__ == "__main__":
    solve()
