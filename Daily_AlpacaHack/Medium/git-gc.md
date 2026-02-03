`.git/logs/HEAD`を確認すると以下のようになっている。

```
> cat .\.git\logs\HEAD
0000000000000000000000000000000000000000 c0bf20c191a250522fc742093ff920243346f578 AlpacaHack <alpacahack@alpacahack.internal> 1767977104 +0900  commit (initial): initial commit
c0bf20c191a250522fc742093ff920243346f578 75a6ad9f0abe942df11f90b58f175d553c23c101 AlpacaHack <alpacahack@alpacahack.internal> 1767977104 +0900  commit: add flag
75a6ad9f0abe942df11f90b58f175d553c23c101 c0bf20c191a250522fc742093ff920243346f578 AlpacaHack <alpacahack@alpacahack.internal> 1767977104 +0900  reset: moving to HEAD~1
```

`commit: add flag`が怪しいので、`git show 75a6ad9f0abe942df11f90b58f175d553c23c101`を実行すると以下のようになる。

```
> git show 75a6ad9f0abe942df11f90b58f175d553c23c101
commit 75a6ad9f0abe942df11f90b58f175d553c23c101
Author: AlpacaHack <alpacahack@alpacahack.internal>
Date:   Sat Jan 10 01:45:04 2026 +0900

    add flag

diff --git a/flag.txt b/flag.txt
new file mode 100644
index 0000000..4c820f2
--- /dev/null
+++ b/flag.txt
@@ -0,0 +1 @@
+Alpaca{--prune=now_1s_4ll_y0u_n33d}
```

このように、履歴からフラグの中身が丸見えになっている。

`git show`は指定したコミットの内容を表示するコマンドで、以下の事が分かる。

- ログメッセージ
- テキストの差分

## 参考文献

[git-show – Git コマンドリファレンス（日本語版）](https://tracpath.com/docs/git-show/)