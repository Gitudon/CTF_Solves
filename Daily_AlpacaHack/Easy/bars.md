普通にWebページを見てもコピーが出来ないので、`curl`コマンドでHTMLを取得してFLAGを得る。

```bash
$ curl -s http://34.170.146.252:55224/ | grep FLAG
  <pre>FLAG: Alpaca{|1||I|l1|IIIl1|1lII|1II|1|I||||1IIlII|11I11II|l11|111l1lllI|I|1|lIIII1I1ll|l1|l1Il1I|11IIl1|1l1IlIII|I1I1I|llllll|l11l1ll11II||||ll11|1lIl11llI1Ill||I1||1|11llIlIIII|IIll1II|lll|I1l||IIIl1I11|1I|III|II|1||1III1I1lllI1l1l|I|1l1lI|II|1|||l|Il|IlII|ll|lIlI1IlIl1Ill11|II111||lI|lII|||IllllIII|l||l|l1Ill}</pre>
```

`pre`タグの中身がFLAGなのでこれをコピーする。