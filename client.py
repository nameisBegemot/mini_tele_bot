import socket
import ssl


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


