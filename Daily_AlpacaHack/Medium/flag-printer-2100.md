1. 以下の`nosleep.c`を作成

```c
unsigned int sleep(unsigned int seconds) {
    return 0; // すぐに終了させる
}
```

1. `nosleep.c`を共有ライブラリとしてコンパイル

```bash
gcc -shared -fPIC nosleep.c -o nosleep.so
```

1. `LD_PRELOAD`を使用して`print_flag`を実行

```bash
LD_PRELOAD=./nosleep.so ./print_flag
```

こうすると、`sleep`関数が上書きされ、ノータイムでフラグが表示される。