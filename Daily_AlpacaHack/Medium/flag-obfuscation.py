import socket
import re

print("IPv6難読化を解除")

# 復元したバイナリデータを格納する配列
exe_data = bytearray()

with open("data.h", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # ダブルクォーテーションで囲まれた文字列（IPv6アドレス）を抽出
        match = re.search(r'"([^"]+)"', line)
        if match:
            ipv6_str = match.group(1)
            try:
                # IPv6の文字列を、16バイトのバイナリデータ（ネットワークバイトオーダ）に逆変換
                chunk = socket.inet_pton(socket.AF_INET6, ipv6_str)
                exe_data.extend(chunk)
            except socket.error as e:
                print(f"[!] 変換エラー: {ipv6_str} ({e})")

# 復元したデータを exe ファイルとして書き出す
output_filename = "recovered.exe"
with open(output_filename, "wb") as f:
    f.write(exe_data)

print(
    f"復元完了！ {len(exe_data)} バイトのデータを '{output_filename}' に保存しました。"
)
# その後、stringコマンドなどでexeファイルからフラグを抽出する
