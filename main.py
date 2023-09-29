import requests
import json
import socket


TOKEN = '1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA'
methodUpdate = 'getUpdates'
methodSendMsg = 'sendMessage'
setWebhook = 'setWebhook'

#https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/setWebhook?url=https://d15d-31-181-124-249.ngrok-free.app
#https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/getWebhookInfo
#https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/setWebhook?url=https://fd85-31-181-124-249.ngrok-free.app&drop_pending_updates=true


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
        conn.close()


server()
