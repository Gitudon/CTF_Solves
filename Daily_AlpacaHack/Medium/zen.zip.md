平文の一部が分かっているので、PKcrackを用いてzipの暗号化を解除する。

まずはPKCrackをインストールする。

```bash
git clone https://github.com/keyunluo/pkcrack.git
cd pkcrack
mkdir build
cd build
cmake ..
make
```

こうすると、`pkcrack/bin`に実行コードが生成される。

`pkcrack/`に平文ファイルを用意する。これは生成コードを読むと分かる。

```bash
python3 -m this >zen.txt
```

そして、`pkcrack/`に暗号化された`zen.zip`も用意し、以下を実行する。

```bash
./bin/pkcrack -C zen.zip -c zen.txt -p zen.txt -d decrypted.zip -a
```

`zen.txt`を`zip`にして`-P zen.zip`をすると良い、ということも調べているうちにあったが今回は必要なかった。

少し待つと、`decrypted.zip`が生成されている。これを解凍すると`flag.txt`が得られる。

```bash
unzip decrypted.zip
```