from socket import *
from time import ctime


HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(family=AF_INET, type=SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(50)

while True:
    print('waiting for connection…')
    tcpCliSock, addr = tcpSerSock.accept()
    print('…connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(b'[%s] %s' % (bytes(ctime(), 'utf-8'), data))

    tcpCliSock.close()
tcpSerSock.close()
