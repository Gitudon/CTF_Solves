from base64 import b16decode, b32decode, b64decode

# 長いのでファイルから読み込み
with open("output.txt", "r") as f:
    encoded_text = f.read().strip()


def detect_encode_type(encoded_text):
    if encoded_text[-1] != "=" and len(encoded_text) % 2 == 0:
        # 末尾に=がなくて、長さが偶数ならbase16の可能性あり
        flag = True
        for e in encoded_text:
            # base16にはA-F, a-f, 0-9しか入っていない
            if e not in "ABCDEFabcdef0123456789":
                flag = False
                break
        if flag:
            return "base16"
    for e in encoded_text:
        # base32にはA-Z, 2-7しか入っていない
        if e not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567=":
            return "base64"
    return "base32"


for _ in range(20):
    encode_type = detect_encode_type(encoded_text)
    print(encode_type)
    if encode_type == "base16":
        encoded_text = b16decode(encoded_text.encode()).decode()
    elif encode_type == "base32":
        encoded_text = b32decode(encoded_text.encode()).decode()
    elif encode_type == "base64":
        encoded_text = b64decode(encoded_text.encode()).decode()

print(encoded_text)
