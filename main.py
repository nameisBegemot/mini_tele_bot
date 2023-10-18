import requests
import json
import socket

import ssl

# TOKEN = '1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA'
# methodUpdate = 'getUpdates'
# methodSendMsg = 'sendMessage'
# setWebhook = 'setWebhook'
#
# ngrok = "https://2ca7-46-159-191-208.ngrok-free.app"

# https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/getUpdates
# https://api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/getFile?file_id=AgACAgIAAxkBAAIBimUeG_bdL4oAATC2j2V1lu0FbsuVvQACGtUxGwVU8Uhrxbtf8dSNtAEAAwIAA3MAAzAE
# https://api.telegram.org/file/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/photos/file_0.jpg

# https://api.telegram.org/file/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/sendSticker?chat_id=<id>&file_id=photos/file_0.jpg

#
# simpl_webhook = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={ngrok}"
# get_webhook = f"https://api.telegram.org/bot{TOKEN}/getWebhookInfo"
# reset_webhook = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={ngrok}&drop_pending_updates=true"
# del_web = f"https://api.telegram.org/bot{TOKEN}/deleteWebhook"

# post_rev = b'''HTTP/1.1 200 OK
# Content-Type: text/html; charset=utf-8
# Content-Length: 16
#
# <h1> hello </h1>
# '''


# def testServ():
#     print("start")
#
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind(('', 9090))
#     sock.listen()
#
#     while True:
#         conn, addr = sock.accept()
#         while True:
#             data = conn.recv(1024)
#
#             if not data:
#                 conn.close()
#                 break
#
#             else:
#                 print("-----------------")
#                 print(data)
#                 print("-----------------")
#                 print(data.decode('UTF-8'))
#
#         conn.close()

#
# def set_webhook():
#     r = requests.get(reset_webhook)
#     print(r.json())


# def del_webhook():
#     r = requests.get(del_web)
#     print(r.json())
#
#
# def get_web():
#     r = requests.get(get_webhook)
#     print(r.json())
#

# def sendMSG(chat_id, text='hi'):
#     # url = f'https://api.telegram.org/bot{TOKEN}/{methodSendMsg}'
#     url = f"https://api.telegram.org/bot{TOKEN}/sendSticker?chat_id={chat_id}&sticker=AgACAgIAAxkBAAIBimUeG_bdL4oAATC2j2V1lu0FbsuVvQACGtUxGwVU8Uhrxbtf8dSNtAEAAwIAA3MAAzAE"
#     a = {'chat_id': chat_id, 'text': '**hello**'}
#     r = requests.post(url, json=a)
#     print(r.json())


# api.telegram.org/bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/getMe

def client():
    message = b'GET /bot1808517150:AAH29icWhsWh-uBG3Icw10wqhYCsb8tf7IA/getMe HTTP/1.1\nHost: api.telegram.org\n\n'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    url = 'api.telegram.org'

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s_sock = context.wrap_socket(sock, server_hostname=url)
    s_sock.connect((url, 443))
    s_sock.send(message)

    data = s_sock.recv(512)

    print(data.decode())

    s_sock.close()
    sock.close()

# def server():
#     print("start")
#
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind(('', 9090))
#     sock.listen()
#
#     while True:
#         conn, addr = sock.accept()
#         while True:
#             data = conn.recv(1024)
#
#             if not data:
#                 conn.close()
#                 break
#
#             else:
#                 print("-----------------")
#                 d = json.loads(data.decode().split("\r\n\r\n")[1])
#                 chat = d['message']['chat']['id']
#                 text = d['message']['text']
#                 print(chat)
#                 print(text)
#
#                 sendMSG(chat)
#                 conn.send(post_rev)
#         conn.close()
#

# hostname = 'api.telegram.org'
# context = ssl.create_default_context()

# Переносы строк лучше явно прописать как \r\n
# В конце должно быть два переноса строки, иначе это не будет считаться полным запросом,
# и сервер будет бесконечно ждать продолжения
# message = b'''GET / HTTP/1.1
# Host: api.telegram.org
#
# '''

# sock = socket.create_connection((hostname, 443))
# ssock = context.wrap_socket(sock, server_hostname=hostname)
# print(ssock.send(message))
# data = ssock.recv(1024)
# print(data.decode())


# message = b'''GET / HTTP/1.1
# Host: api.telegram.org
#
# '''

# def client():
#     message = b'GET / HTTP/1.1\nHost: api.telegram.org\n\n'
#
#     # message = b'''GET / HTTP/1.1
#     # Host: api.telegram.org
#     #
#     # '''
#
#     print(message)
#
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     url = 'api.telegram.org'
#
#     context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#     s_sock = context.wrap_socket(sock, server_hostname=url)
#     s_sock.connect((url, 443))
#     s_sock.send(message)
#
#
#     data = s_sock.recv(512)
#
#     print(data.decode())
#
#     s_sock.close()
#     sock.close()

client()