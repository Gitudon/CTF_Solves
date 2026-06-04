ペイロードは以下。

```javascript
this.constructor.constructor("return process.env.FLAG")()
```

`this`サンドボックス内で実行されている現在のコンテキスト（グローバルオブジェクト）を指す。

`this.constructor`そのオブジェクトを生成したコンストラクタ（通常は Object 関数）にアクセスする。

`this.constructor.constructor`関数のコンストラクタ、つまり「関数を生み出すための関数(`Function`)」にアクセスする。この Function は、サンドボックスの外側（メインプロセス側）のコンテキストで実行されている。

`Function("...")()`外側の世界で新しい関数を作成して実行するため、サンドボックスの壁を完全に無視してメインプロセスの`process`オブジェクトを呼び出すことができる。

これによって、環境変数`process.env.FLAG`の中身をそのまま`console.log`で出力させることが可能になる。