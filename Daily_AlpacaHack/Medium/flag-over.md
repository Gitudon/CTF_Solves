サブプロセスで環境変数は書き換えられているので、普通に確認しても無理。

```bash
$ echo $FLAG
echo $FLAG
🦙
```

しかし、親プロセスはまだ生きているので、実行中の全プロセスの環境変数を確認すれば、変更前のFLAGが見つかる。

プロセスの情報は`/proc/`以下にある。以下のコマンドでPythonプロセスの環境変数に絞って確認すればよい。

```
$ cat /proc/$(pgrep -o python)/environ | tr '\0' '\n' | grep FLAG
<pgrep -o python)/environ | tr '\0' '\n' | grep FLAG
FLAG=Alpaca{daaaaamn_next_overwrite_everything!!!!}
```

