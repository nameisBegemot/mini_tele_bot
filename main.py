import requests
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
Content-Length: 16

<h1> hello </h1>
'''

TOKEN = '1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA'
methodUpdate = 'getUpdates'
methodSendMsg = 'sendMessage'
setWebhook = 'setWebhook'


#https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/setWebhook?url=https://d15d-31-181-124-249.ngrok-free.app
#https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/getWebhookInfo
#https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/setWebhook?url=https://9682-31-181-124-249.ngrok-free.app&drop_pending_updates=true

def sendMSG(chat_id, text='hi'):
    url = f'https://api.telegram.org/bot{TOKEN}/{methodSendMsg}'
    a = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=a)


def server():
    print("start")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 8443))
    sock.listen()

    conn, addr = sock.accept()

    #print(conn, addr)


    while True:
        data = conn.recv(1024)

        if not data:
            break
        print("-----------------")

        d = json.loads(data.decode().split("\r\n\r\n")[1])

        chat = d['message']['chat']['id']
        text = d['message']['text']

        print(chat)
        print(text)

        sendMSG(chat)

        #conn.send(f)

    conn.close()


def up():
    api = f'https://api.telegram.org/bot{TOKEN}/{methodUpdate}'
    r = requests.get(api)
    print(r.json()['result'][-1]['message']['text'])

server()
