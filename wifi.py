import network
import time
import config 

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(config.SSID, config.PASSWORD)  # config.pyから設定情報を取得
    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected to Wi-Fi!")
    print("IP Address:", wlan.ifconfig()[0])
