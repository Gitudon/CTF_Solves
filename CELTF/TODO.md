以下のcurlコマンドを実行すると、ターゲットユーザーの情報がJSON形式で取得できる。

```
curl 'http://target1.jail.celtf.com/api/user/jail_target1@example.com' \
  -H 'Accept: */*' \
  -H 'Accept-Language: ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7' \
  -H 'Connection: keep-alive' \
  -H 'Referer: http://target1.jail.celtf.com/' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0' \
  --insecure
```

これを使ってログインすると、以下の情報を得る。

- ログイン用のトークン
  - フラグ1個目
- 預かった認証トークンのダウンロード用URL
  - URLの中にフラグっぽいUUIDがあったがフラグではないらしい
- ログイン用のトークンを暗号化したもの
  - 暗号化方式のヒント

DLしたファイルは暗号化されていて読めない