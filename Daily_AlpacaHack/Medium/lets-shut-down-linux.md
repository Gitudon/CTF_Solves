Linuxで`reboot`システムコールによりシャットダウンを行いたいので、`magic`に`LINUX_REBOOT_MAGIC1`、`magic2`に`LINUX_REBOOT_MAGIC2`、そして`cmd`に`LINUX_REBOOT_CMD_POWER_OFF`を指定すればよい。

これらの値を調べると以下の通り。

```
LINUX_REBOOT_MAGIC1 = 0xfee1dead
LINUX_REBOOT_MAGIC2 = 672274793
LINUX_REBOOT_CMD_POWER_OFF = 0x4321fedc
```

今回引数には数字しか含められないので、これらを必要に応じて16進数から10進数に変換したものを入力すればフラグが入手できる。

```
>>> int("0xfee1dead", 16)
4276215469
>>> int("0x4321fedc", 16)
1126301404
```

## 参考文献

https://kazmax.zpp.jp/cmd/r/reboot.2.html