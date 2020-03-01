from twisted.internet import protocol, reactor
from time import ctime


class ServerProtocol(protocol.Protocol):
    def connectionMade(self):
        print("...connected from %s" % self.transport.getPeer().host)

    def dataReceived(self, data):
        self.transport.write(b"[%b] %b" % (ctime().encode("utf-8"), data))


class ServerFactory(protocol.Factory):
    protocol = ServerProtocol


print("...waiting for connection")
reactor.listenTCP(32222, ServerFactory())
reactor.run()