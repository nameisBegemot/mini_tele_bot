import requests
import json
import socket


TOKEN = '1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA'
methodUpdate = 'getUpdates'
methodSendMsg = 'sendMessage'
setWebhook = 'setWebhook'

ngrok = "https://38aa-31-181-124-249.ngrok-free.app"

simpl_webhook = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={ngrok}"
get_webhook = f"https://api.telegram.org/bot{TOKEN}/getWebhookInfo"
reset_webhook = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={ngrok}&drop_pending_updates=true"
del_web = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"


post_rev = b'''HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 16

<h1> hello </h1>
'''


def set_webhook():
    r = requests.get(reset_webhook)
    print(r.json())


def del_webhook():
    r = requests.get(del_web)
    print(r.json())


def get_web():
    r = requests.get(get_webhook)
    print(r.json())


def sendMSG(chat_id, text='hi'):
    url = f'https://api.telegram.org/bot{TOKEN}/{methodSendMsg}'
    a = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=a)


def server():
    print("start")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9090))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        while True:
            data = conn.recv(1024)

            if not data:
                conn.close()
                break

            else:
                print("-----------------")
                d = json.loads(data.decode().split("\r\n\r\n")[1])
                chat = d['message']['chat']['id']
                text = d['message']['text']
                print(chat)
                print(text)

                sendMSG(chat)
                conn.send(post_rev)
        conn.close()


get_web()

