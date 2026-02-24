まずapkファイルをGhidraにインポートすると、以下のような3つのdexファイルが見つかります。

```
classe.dex
classes2.dex
classes3.dex
```

このうち、classes3.dexでSymbol Treeを展開し、`Alpaca`などといった単語で検索していると、`Namespaces`の中に`string_data`なるものがあり、まんまフラグの文字列が見つかりました。

```
Alpaca{h0w_d1d_y0u_b34t_th3_4lp4c4}
```