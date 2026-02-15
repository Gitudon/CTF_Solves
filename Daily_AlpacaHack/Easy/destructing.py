from pwn import *


# キーにダブルクォートを追加する関数
def add_double_quote(q: str) -> str:
    buf = ""
    for c in q:
        if "a" <= c <= "z":
            buf += '"' + c + '"'
        else:
            buf += c
    return buf


# 受け取ったJSONを加工して、正しい形式にする関数
def make_the_answer(q: str) -> str:
    q = add_double_quote(q)
    return (
        q.replace("_", "")
        .replace(", , ,", ", null, null,")
        .replace(", ,", ", null,")
        .replace("[, ", "[null, ")
        .replace(", ]", ", null]")
    )


def main():
    # リモートサーバーに接続
    io = remote("34.170.146.252", 25646)
    for _ in range(5):
        # ステージを表示
        print(io.recvline().decode())
        # 壊れたJSONを受け取る
        received_json = io.recvline().decode()[6:-9]
        print(f"Received JSON: {received_json}")
        # JSONを加工して正しい形式にする
        answer = make_the_answer(received_json)
        print(f"Answer: {answer}")
        # 加工したJSONを送信
        io.sendlineafter(b"json> ", answer.encode())
        # ステージの結果を表示
        print(io.recvline().decode())
        # 空行を飛ばす
        io.recvline()
    # 最後にフラグを受け取る
    print(io.recvline().decode())


if __name__ == "__main__":
    main()
