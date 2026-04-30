接続したら、まず本物の`chal.sh`を退避させる。中身は見えないが、カレントディレクトリの権限が自分にあるのでリネームが可能。

```bash
mv chal.sh chal.sh.bak
```

次に偽の`chal.sh`を作成する。

```bash
echo '#!/bin/sh' > chal.sh
echo 'cat flag.txt' >> chal.sh
chmod +x chal.sh
```

一回接続を切り、再接続する。するとサーバは`chal.sh`を`root`権限で実行しようとするが、中身は偽物になっているので、結果`cah flag.txt`が`root`権限で実行され、フラグが表示される。