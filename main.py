
import json
import socket

import requests

# from client import *
import templates as ts


import ssl


TOKEN = '1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA'
methodUpdate = 'getUpdates'
methodSendMsg = 'sendMessage'
setWebhook = 'setWebhook'

ngrok = "https://6a45-31-181-70-93.ngrok-free.app"

# https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/getUpdates
# https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/getFile?file_id=AgACAgIAAxkBAAIBimUeG_bdL4oAATC2j2V1lu0FbsuVvQACGtUxGwVU8Uhrxbtf8dSNtAEAAwIAA3MAAzAE
# https://api.telegram.org/file/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/photos/file_0.jpg
#
# https://api.telegram.org/file/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/sendSticker?chat_id=<id>&file_id=photos/file_0.jpg


simpl_webhook = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={ngrok}"
get_webhook = f"https://api.telegram.org/bot{TOKEN}/getWebhookInfo"
reset_webhook = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={ngrok}&drop_pending_updates=true"
del_web = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"




post_rev = b'''HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 0

'''

# noinspection PyByteLiteral
post_send = b'GET /bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/sendMessage?chat_id=976522178&text="hello" HTTP/1.1\r\n' \
            b'Host: api.telegram.org\r\n' \
            b'Content-Length: 45\r\n' \
            b'Content-Type: application/json\r\n'








# https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/sendMessage?chat_id=976522178&text='hello'


# def sendMSG(chat_id, text='hi'):
#     url = f'https://api.telegram.org/bot{TOKEN}/{methodSendMsg}'
#     # url = f"https://api.telegram.org/bot{ts.TOKEN}/sendSticker?chat_id={chat_id}&sticker=AgACAgIAAxkBAAIBimUeG_bdL4oAATC2j2V1lu0FbsuVvQACGtUxGwVU8Uhrxbtf8dSNtAEAAwIAA3MAAzAE"
#     a = {'chat_id': chat_id, 'text': '**hello**'}
#     r = requests.post(url, json=a, stream=True)
#     print(r.content)


# api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/getMe


# def client2():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     url = 'api.telegram.org'
#
#     sock.connect((url, 443))
#     sock.send(post_send)
#
#     data = sock.recv(512)
#
#     print(data.decode())
#
#     sock.close()


def client(chat, text = "hello"):
    pp = f'POST /bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/sendMessage?chat_id={chat}&text={text} HTTP/1.1\r\n' \
    'Host: api.telegram.org\r\n' \
    'User-Agent: python-requests/2.31.0\r\n' \
    'Accept-Encoding: gzip, deflate\r\n' \
    'Accept: */*\r\n' \
    'Connection: keep-alive\r\n' \
    'Content-Length: 0\r\n' \
    '\r\n\r\n'

    # message = b'GET /bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/getMe HTTP/1.1\nHost: api.telegram.org\n\n'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    url = 'api.telegram.org'

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s_sock = context.wrap_socket(sock, server_hostname=url)
    s_sock.connect((url, 443))
    s_sock.send(pp.encode())
    print(pp)

    data = s_sock.recv(512)

    print(data.decode())

    s_sock.close()
    sock.close()


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
                # print(chat)
                client(chat, text)

                # sendMSG(chat)
                conn.send(post_rev)
        conn.close()


def set_webhook():
    r = requests.get(reset_webhook)
    print(r.json())

def del_webhook():
    r = requests.get(del_web)
    print(r.json())
#

del_webhook()
set_webhook()
server()
#
# from requests_toolbelt.utils import dump
#
#
# r = requests.post("https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/sendMessage?chat_id=976522178&text='hello'")
#
# data = dump.dump_all(r)
# print(data.decode('utf-8'))

