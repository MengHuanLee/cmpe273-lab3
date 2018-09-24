from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        host = "10.63.194.100"
        port = 1234
        #client connects to server and send message
        self.transport.connect(host, port)
        self.transport.write(bytes("Hello World", 'utf-8'))

    def datagramReceived(self, data, addr, port):
        data = data.decode()  # remove the annoying 'b' prefix
        print("received %r from server" % data, str(addr[0]) + ":" + str(addr[1]))

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")

# 0 means any port, we don't care in this case
reactor.listenUDP(0, Helloer())
reactor.run()