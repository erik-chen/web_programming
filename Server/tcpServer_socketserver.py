from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime


HOST = 'localhost'
PORT = 21588
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from', self.client_address)
        self.wfile.write(b'[%s] %s' % (ctime().encode('utf-8'), self.rfile.readline()))


tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection')
tcpServ.serve_forever()
