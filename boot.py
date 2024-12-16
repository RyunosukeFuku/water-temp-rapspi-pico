import socket
import wifi
import http_client

# Wi-Fi接続
wifi.connect()

def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        try:
            request = cl.recv(1024).decode('utf-8')
            print("Request:")
            print(request)
            if "POST /measure_and_send" in request:
                http_client.measure_and_send()
                response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nMeasurement sent!"
            else:
                response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\nNot Found"
            cl.send(response)
        except Exception as e:
            print("Error:", e)
        finally:
            cl.close()

# サーバー開始
start_server()
