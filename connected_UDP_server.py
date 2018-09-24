from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        #Server started
        #print("Listening at port", port)
        pass

    def datagramReceived(self, data, host):

        print("Received message from client", str(host[0]), ":", str(host[1]), data.decode('utf-8'))

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")

# 0 means any port, we don't care in this case
reactor.listenUDP(1234, Helloer())
reactor.run()