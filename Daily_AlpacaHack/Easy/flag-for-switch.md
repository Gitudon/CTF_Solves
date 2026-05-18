このサイトでSwitchのユーザーエージェントがわかる。

https://user-agents.net/string/mozilla-5-0-nintendo-switch-webapplet-applewebkit-609-4-khtml-like-gecko-nf-6-0-2-20-5-nintendobrowser-5-1-0-22023-dalvik-2-1-0-linux-u-android-5-1-1-aeobc-build-lvy48f


あとはこれを使ってcurlコマンドを作ればよい。ペイロードは以下。

```bash
curl -H "User-Agent: Mozilla/5.0 (Nintendo Switch; WebApplet) AppleWebKit/609.4 (KHTML, like Gecko) NF/6.0.2.20.5 NintendoBrowser/5.1.0.22023 Dalvik/2.1.0 (Linux; U; Android 5.1.1; AEOBC Build/LVY48f)" http://34.170.146.252:13697/
```