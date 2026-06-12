`openssl`コマンドを使って証明書情報を抜き出すと、その中にフラグが含まれていることがわかる。

```bash
openssl s_client -connect 34.170.146.252:21751  2>/dev/null | openssl x509 -text
```

分かりづらい場合は`grep`する。

```bash
openssl s_client -connect 34.170.146.252:21751  2>/dev/null | openssl x509 -text | grep Alpaca{
```