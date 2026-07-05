以下のJavaScriptをコンソールに貼り付けて1ミリ間隔で連打させる。

```javascript
const targetSelector = 'p';

const intervalTime = 1;

const intervalId = setInterval(() => {
    const button = document.querySelector(targetSelector);
    if (button) {
        button.click();
    } else {
        console.log('対象が見つかりません');
        clearInterval(intervalId);
    }
}, intervalTime);

// 停止したい場合はコンソールに以下を入力
// clearInterval(intervalId);
```

ちょっと時間がかかるが、毎秒1000回で10万回なので数分くらい。