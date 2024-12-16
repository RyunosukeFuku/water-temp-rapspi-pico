import urequests
import sensors
import config  # 設定ファイルをインポート


def measure_and_send():
    #url = "http://受け取るサーバのIP:8080/src/receive_data.php"
    url = config.SERVER_URL  # 設定ファイルからURLを取得


    temperature = sensors.get_temperature()
    payload = {
        "temperature": temperature,
    }
    headers = {'Content-Type': 'application/json'}

    try:
        response = urequests.post(url, json=payload, headers=headers)
        print("Server response:", response.text)
    except Exception as e:
        print("Failed to send data:", e)
