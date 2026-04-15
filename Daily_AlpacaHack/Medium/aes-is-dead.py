from collections import Counter

# 暗号化されたファイルを読み込む
with open("flag.enc", "rb") as f:
    data = f.read()

# 16バイトごとのブロックに分割
blocks = [data[i : i + 16] for i in range(0, len(data), 16)]

# 一番多く出現するブロック（＝画像の白い背景部分）を特定
most_common_block = Counter(blocks).most_common(1)[0][0]

# 視覚化データの生成
out = bytearray()
for b in blocks:
    if b == most_common_block:
        out.extend(b"\xff" * 16)  # 背景を「白」に
    else:
        out.extend(b"\x00" * 16)  # それ以外（文字部分）を「黒」に

# 生データとして保存
with open("flag_visual.raw", "wb") as f:
    f.write(out)

print("抽出完了！ flag_visual.raw をGIMPなどで開いてください。")
# GIMPで開き、幅を適当に設定、場合に応じて反転を使ってFLAGを読む。
