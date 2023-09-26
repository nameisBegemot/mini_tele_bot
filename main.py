#import requests
import json
import socket


# def bot():
#     TOKEN = '1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA'
#     t = 'https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/getUpdates'
#     r = requests.get(t)
#     print(r.json())



gg = b'''HTTP/1.1 200 OK
Server: YarServer/2009-09-09
Content-Type: text/html
Content-Length: 123
Connection: close

<h1> Hello </h1>'''


f = b'''HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 129

<h1> hello </h1>
'''


def server():
    print("start")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9090))
    sock.listen()

    conn, addr = sock.accept()

    print(conn, addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f)
        conn.send(f)


    conn.close()


server()
