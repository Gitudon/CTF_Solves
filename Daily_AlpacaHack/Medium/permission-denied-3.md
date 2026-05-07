`/proc`に残っている`chal.sh`の残骸からFLAGを読み取る。

```
$ nc 34.170.146.252 19723
# find /proc/*/fd -ls 2>/dev/null | grep deleted
  7126091      0 lr-x------   1 root     root           64 May  7 16:59 /proc/8/fd/255 -> /app/chal.sh\ (deleted)
# cat /proc/8/fd/255
echo Alpaca{h4s_ABS0LU73_p3rm1ss10ns_0v3r_3v3ry7h1ng} |
install -m 400 /dev/stdin flag.txt
rm *
sh
```