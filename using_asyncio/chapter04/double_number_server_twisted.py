from twisted.internet import reactor, protocol


class DoubleNumber(protocol.Protocol):
    def connectionMade(self):
        msg = "Welcome to DoubleNumber server \n"
        self.transport.write(msg.encode("utf-8"))

    def dataReceived(self, data: bytes):
        # data sent by telnet when you press Ctrl+C in the terminal
        if data == b"\xff\xf4\xff\xfd\x06":
            self.transport.loseConnection()
            return
        str_number = data.decode("utf-8").strip()
        try:
            double_number = int(str_number) * 2
            msg = f"{str_number} x 2 = {double_number}"
        except ValueError:
            msg = f"The data sent ({str_number}) is not a integer"
        self.transport.write((msg + "\n").encode("utf-8"))

    def connectionLost(self, reason):
        print("connection lost")


if __name__ == "__main__":
    print("Running DoubleNumber Server")
    factory = protocol.ServerFactory()
    factory.protocol = DoubleNumber
    reactor.listenTCP(5555, factory)
    reactor.run()
