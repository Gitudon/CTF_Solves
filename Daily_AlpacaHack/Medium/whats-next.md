開発者ツールでトップページの通信一覧を見てみると、`_buildManifest.js`といういかにもなものがあった。

そのプレビューを見てみると以下のようになっていた。

```js
self.__BUILD_MANIFEST = {
  "/": [
    "static/chunks/82e29a3e3a5232ab.js"
  ],
  "/_error": [
    "static/chunks/0bd39797e29cb6db.js"
  ],
  "/secret-5Q940Ja1Csr0yHW5e0N9CQd3NpUVk0Ru": [
    "static/chunks/dfe742b27c8089ba.js"
  ],
  "__rewrites": {
    "afterFiles": [],
    "beforeFiles": [],
    "fallback": []
  },
  "sortedPages": [
    "/",
    "/_app",
    "/_error",
    "/secret-5Q940Ja1Csr0yHW5e0N9CQd3NpUVk0Ru"
  ]
};self.__BUILD_MANIFEST_CB && self.__BUILD_MANIFEST_CB()
```

以下のようなcurlコマンドでも取得できる。

```bash
curl 'http://34.170.146.252:12651/_next/static/c3MnYZtavUfl8ZwYGdIUd/_buildManifest.js'
```

`/secret-5Q940Ja1Csr0yHW5e0N9CQd3NpUVk0Ru`というページがあることがわかる。これが対象ページである。アクセスしてみると、フラグが表示された。

```bash
curl http://34.170.146.252:12651/secret-5Q940Ja1Csr0yHW5e0N9CQd3NpUVk0Ru
```