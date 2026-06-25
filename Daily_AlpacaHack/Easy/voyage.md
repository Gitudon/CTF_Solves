以下のコマンドを利用すると`cpio`を解凍できる。なんか警告が出るが大丈夫そう。

```
$ cpio -id --no-preserve-owner < initramfs.cpio
cpio: dev/null: Cannot mknod: Operation not permitted
cpio: dev/ttyS0: Cannot mknod: Operation not permitted
cpio: dev/console: Cannot mknod: Operation not permitted
4159 blocks
```

解凍したあと`flag.txt`が出現している。

```
$ ls
bin  bzImage  dev  etc  flag.txt  home  init  initramfs.cpio  print_flag.py  proc  run.sh  sbin  sys  tmp  usr
```

`flag.txt`はこのままでは読めない。

```
$ cat flag.txt
ɩ�ɩ��ɩ�Eɩ�ɫ�ɫ�ɫ�ɫ�ɩ�Eɩ��ɩ�EŔ�ɫ�ɫ�ɫ�Ŕ�Eɩ��ɩ�Ŕ�ɫ�ɫ�ɩ�ȳ� LFKM
CY
BOXO
YuMO^uY^KX^ONu]C^BuAOXDOFuORZFEC^Y




                                  W
```

そこで、親切にも用意されている`print_flag.py`を利用する。コードの中にパスを書く所があるのでそこに`flag.txt`と書くとフラグを確認できる。

```
$ python3 print_flag.py
```