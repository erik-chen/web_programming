from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


while True:
    tcpCliSock = socket(family=AF_INET, type=SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8')+b'\r\n') # add b'\r\n'
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip().decode('utf-8'))
    tcpCliSock.close()
