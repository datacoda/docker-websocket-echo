from autobahn.websocket import WebSocketServerProtocol


class EchoServerProtocol(WebSocketServerProtocol):

    def onMessage(self, msg, binary):
        self.sendMessage(msg, binary)


if __name__ == '__main__':
    import sys

    from autobahn.websocket import listenWS, WebSocketServerFactory
    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)

    port = int(sys.argv[1])
    binding = port
    if (len(sys.argv) > 2):
        binding = int(sys.argv[2])

    print "Setting websocket port %d=>%d(bind)" % ( port, binding )
    factory = WebSocketServerFactory("ws://localhost:%d" % ( binding ),
                                     externalPort = port,
                                     debug = False)
    factory.protocol = EchoServerProtocol

    listenWS(factory)
    reactor.run()