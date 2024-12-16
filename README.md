# 水温管理システム連動ラズパイピコW

## 概要

水温管理システムは、ラズパイで測った水温(または気温)を管理するためのシステムです。

![UML図](https://github.com/RyunosukeFuku/water-temp-monitor/blob/master/images/uml.png)

受信側の管理マシン
https://github.com/RyunosukeFuku/water-temp-monitor

## 設定
config.pyで自身の環境変数を定義してあげる必要がある

```python:config.py
# Wi-Fi設定情報
SSID = "WIFIネットワーク名"
PASSWORD = "WIFIパスワード"

# サーバー設定
SERVER_URL = "http://受信側マシンのIP:ポート/src/receive_data.php"
```





