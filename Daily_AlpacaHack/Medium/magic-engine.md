`default.conf`を覗いてみると、以下の様にフラグが含まれているファイル名が記載されていることがわかります。

```
server {
    listen 80;
    server_name admin.alpaca.secret;

    root /usr/share/nginx/html;

    location = / {
        try_files /secret.html =404;
    }
}
```

とりあえず`http://34.170.146.252:52496/secret.html`にアクセスしてみたら、フラグが表示されました。

```
$ curl http://34.170.146.252:52496/secret.html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Magic Engine - secret</title>
</head>
<body>
  <h1>Secret page</h1>
  <p>Wow, how did you get here?</p>
  <p>Alpaca{Host_works_just_like_Magic}</p>
</body>
</html>
```

実際は、以下のように`Host`ヘッダーを指定してアクセスする必要があるみたいです。

```bash
curl -H "Host: admin.alpaca.secret" http://34.170.146.252:52496/secret.html
```

参考: https://www.notion.so/kakur41-wrteup/Daily-AlpacaHack-2-1-2-7-301da8520c0280a3b097dbe2dddf0deb