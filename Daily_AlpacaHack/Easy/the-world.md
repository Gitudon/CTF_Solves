律儀に時間を合わせようとすると難しいので、別の手段で解きます。

変数`FLAG`にフラグが格納されているので、それを入力するとエラーメッセージにフラグが表示されます。

```
$ nc 34.170.146.252 23758
[Warmup] current time (seconds)?
FLAG
server.sh: line 6: Alpaca{muda.sh}: arithmetic syntax error: invalid arithmetic operator (error token is "{muda.sh}")
server.sh: line 7: d1: unbound variable
```