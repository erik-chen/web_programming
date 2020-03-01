from twisted.internet import protocol, reactor
from time import ctime


PORT = 21567


class TSSerProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.transport.getPeer().host
        print('connected from', clnt)

    def dataReceived(self, data):
        self.transport.write(b'[%s] %s' % (ctime().encode('utf-8'), data))


factory = protocol.Factory()
factory.protocol = TSSerProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()