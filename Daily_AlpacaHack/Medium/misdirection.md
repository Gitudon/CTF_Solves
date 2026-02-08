逆コンパイルすると逆に分からなくなる問題らしい。

以下のコマンドを用いてフラグに関する部分を抜き出す。

```bash
$ strings -a ./misdirection | grep "Alpaca{"
```

すると以下のような文字列が得られる。

```
}detpecca_si_galf_siht_yhw_dnatsrednu_s'teL_!stargnoC{acaplAlpaca{This_is_NOT_a_flag_This_must_be_rejected_by_program!}
```

後半の`Alpaca{This_is_NOT_a_flag_This_must_be_rejected_by_program!}`はフラグではない。

前半部分を逆順に読むと以下のようになる。

```
Alpaca{Congrats!_Let's_understand_why_this_flag_is_accepted}
```

これが正解となる。