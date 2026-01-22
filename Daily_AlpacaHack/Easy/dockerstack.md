与えられた`tar`ファイルを解凍

```bash
$ mkdir extracted-image
$ tar -xf output-image.tar -C extracted-image
$ cd extracted-image
```

`tree`コマンドでディレクトリ構造を確認

```
$ tree
.
├── blobs
│   └── sha256
│       ├── 0531badbea1bbfd8db4244371c4c89e587f729a37c1dbf6dbc75a89bb09e003c
│       ├── 265c6b6c91fb0cab080e43824b80565687c834631d570b43ba64196e8a6bb20b
│       ├── 471fc30039fcb37e84aa6eede49db36e835d6aceb1185dc58a0250ada68f669a
│       ├── 7bb20cf5ef67526cb843d264145241ce4dde09a337b5be1be42ba464de9a672d
│       ├── 8ead43c9e5e2607adbec457f4acb3f83f6bbd8412566f5878e47835e12694b15
│       ├── 935c27cb58c708339646345ed7315a401c2cab8aa2733ba41aecb896c7e1566c
│       ├── c57a625e7523f654b7256b33b17e43cf74c8650bd1a441884a70615d7327b85b
│       ├── d4d3fcdccbfd98ebe464c41932cea2bcb0d67149e0375cd6fdd28fb56f7f9007
│       ├── ddceb7aa914367258c7573c22a200ef88612608dfc3694102256cc1076b3fcbd
│       └── eb5955df1e75829e5eeb5b71b724a1351cb08fb6b989c107c31dbc25856f2db9
├── index.json
├── manifest.json
├── oci-layout
└── repositories

3 directories, 14 files
```

`manifest.json`を確認

```json
"Layers":["blobs/sha256/7bb20cf5ef67526cb843d264145241ce4dde09a337b5be1be42ba464de9a672d","blobs/sha256/c57a625e7523f654b7256b33b17e43cf74c8650bd1a441884a70615d7327b85b","blobs/sha256/265c6b6c91fb0cab080e43824b80565687c834631d570b43ba64196e8a6bb20b","blobs/sha256/0531badbea1bbfd8db4244371c4c89e587f729a37c1dbf6dbc75a89bb09e003c"]
```

これの2番目のレイヤーが`RUN rm flag.b64.txt`で削除されたファイルを含んでいる可能性が高いので、展開してみる。

```
$ tar -tf blobs/sha256/265c6b6c91fb0cab080e43824b80565687c834631d570b43ba64196e8a6bb20b | grep flag
flag.b64.txt
```

`flag.b64.txt`を抽出

```bash
$ tar -xf blobs/sha256/265c6b6c91fb0cab080e43824b80565687c834631d570b43ba64196e8a6bb20b app/flag.b64.txt
$ cat app/flag.b64.txt
e0RvY2tlcl9kZV9kb2trYW4hfQ
```

デコードしてフラグを取得

```bash
$ echo 'e0RvY2tlcl9kZV9kb2trYW4hfQ' | base64 -d
{Docker_de_dokkan!}
```

これの最初に`Alpaca`を付けるとフラグが完成する

```
Alpaca{Docker_de_dokkan!}
```