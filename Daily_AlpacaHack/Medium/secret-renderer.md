`http://34.170.146.252:[port]/report`で以下のURLにレポートをする。

```
http://nginx:3000/render/a.css
```

その後、以下のURLにキャッシュが出来ているので、ページにアクセスするとフラグを獲得できる。

```
http://34.170.146.252:[port]/render/a.css
```