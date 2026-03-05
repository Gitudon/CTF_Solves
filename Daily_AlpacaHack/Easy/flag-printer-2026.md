`Dockerfile`を見ると次のような記述がある。

```Dockerfile
CMD ["socat", "-T5", "tcp-listen:1337,fork,reuseaddr", "exec:'python server.py'"]
```

これは「5秒でタイムアウトする」ということ。なので、ただ単純に`nc`で接続しても、5秒後には切断されてしまう。

そこで、以下のワンライナーを用いて、「空文字列を2秒ごとに送信し続ける」ということをする。これにより通信が続いていると判断され、タイムアウトされることなくFLAGの表示を待つことができる。

```bash
(while true; do sleep 2; echo ""; done) | nc 34.170.146.252 10951
```