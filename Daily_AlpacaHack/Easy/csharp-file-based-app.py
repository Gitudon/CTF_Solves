import base64
import brotli

encoded = "GzMA+MVtbG/XtFYgGNGLSpSiwoAdaiYvxraqBw=="

# 1. Base64デコード
compressed_data = base64.b64decode(encoded)

# 2. Brotli解凍 & UTF-8文字列化
flag = brotli.decompress(compressed_data).decode("utf-8")

print(flag)
